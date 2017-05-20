#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from unittest import TestCase

import unittest
from unipath import Path
from mock import Mock, MagicMock, patch

from antlr4 import InputStream, ParseTreeWalker
from antlr4.CommonTokenStream import CommonTokenStream


from scikit_fuzzy_fcl.FclLexer import FclLexer
from scikit_fuzzy_fcl.FclListener import FclListener
from scikit_fuzzy_fcl.FclParser import FclParser


TESTS_DIR = Path(__file__).ancestor(1)
FIXTURES_DIR = TESTS_DIR.child('fixtures')


class FclListenerTester(FclListener):

    def __init__(self):
        super(FclListenerTester, self).__init__()
        self.function_blocks_ids = []
        self.inputs = []
        self.outputs = []
        self.fuzzyfy_blocks = []
        self.last_var_def = None
        self.last_linguistic_terms = []

    def enterFunction_block(self, ctx):
        f_id = ctx.ID()
        if f_id:
            self.function_blocks_ids.append(ctx.ID().getText())

    def exitVar_input(self, ctx):
        if self.last_var_def:
            self.inputs.append(self.last_var_def)
        self.last_var_def = None

    def exitVar_output(self, ctx):
        if self.last_var_def:
            self.outputs.append(self.last_var_def)
        self.last_var_def = None

    def enterVar_def(self, ctx):
        self.last_var_def = [ctx.ID().getText(), ctx.data_type().getText()]
        vrange = ctx.vrange()
        if vrange:
            self.last_var_def.extend(real.getText() for real in vrange.REAL())

    def exitFuzzify_block(self, ctx):
        fuzzyfy_block = {
            'id': ctx.ID().getText(),
            'linguistic_term': self.last_linguistic_terms
        }
        self.fuzzyfy_blocks.append(fuzzyfy_block)
        self.last_linguistic_terms = []

    def enterLinguistic_term(self, ctx):
        mf = ctx.membership_function()

        self.last_linguistic_terms.append({
            'id': ctx.ID().getText(),
            'mf': mf.getText(),
        })

    def exitPiece_wise_linear(self, ctx):
        points = []
        for point in ctx.points():
            points.append([point.atom()[0].getText(), point.atom()[1].getText()])
        self.last_piece_wise_liner = points

    def exitSingletons(self, ctx):
        points = []
        for point in ctx.points():
            points.append([point.atom()[0].getText(), point.atom()[1].getText()])
        self.last_singletons = points

    def exitDefuzzify_block(self, ctx):
        defuzz_items = ctx.defuzzify_item()
        items = None
        if defuzz_items:
            items = [i.getText() for i in defuzz_items]
        self.last_defuzz = {'id': ctx.ID().getText(), 'items': items}

    def exitDefault_value(self, ctx):
        value = ctx.REAL() or ctx.NC()
        self.last_default_value = value.getText()


class TestFclGrammar(unittest.TestCase):

    def test_load_simple_function_block(self):
        fcl_text = """
        FUNCTION_BLOCK f_block1_name
        END_FUNCTION_BLOCK
        """
        lexer = FclLexer(InputStream(fcl_text))
        stream = CommonTokenStream(lexer)
        parser = FclParser(stream)
        tree = parser.main()
        listener = FclListenerTester()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

        self.assertEqual('f_block1_name', listener.function_blocks_ids[0])

    def test_load_simple_function_block2(self):
        fcl_text = """
        FUNCTION_BLOCK
        END_FUNCTION_BLOCK
        """
        lexer = FclLexer(InputStream(fcl_text))
        stream = CommonTokenStream(lexer)
        parser = FclParser(stream)
        tree = parser.main()
        listener = FclListenerTester()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

        self.assertEqual([], listener.function_blocks_ids)

    def test_load_simple_function_block3(self):
        fcl_text = """
        FUNCTION_BLOCK a
        END_FUNCTION_BLOCK
        FUNCTION_BLOCK b
        END_FUNCTION_BLOCK
        """
        lexer = FclLexer(InputStream(fcl_text))
        stream = CommonTokenStream(lexer)
        parser = FclParser(stream)
        tree = parser.main()
        listener = FclListenerTester()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

        self.assertEqual(['a', 'b'], listener.function_blocks_ids)

    def test_var_input(self):
        fcl_text = """
        FUNCTION_BLOCK f_block
            VAR_INPUT
                input_id : REAL;
            END_VAR
        END_FUNCTION_BLOCK
        """
        lexer = FclLexer(InputStream(fcl_text))
        stream = CommonTokenStream(lexer)
        parser = FclParser(stream)
        tree = parser.main()
        listener = FclListenerTester()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

        self.assertEqual(['input_id', 'REAL'], listener.inputs[0])

    def test_var_input_range(self):
        fcl_text = """
        FUNCTION_BLOCK f_block
            VAR_INPUT
                input_id : REAL; RANGE := ( 12 .. 34 );
            END_VAR
        END_FUNCTION_BLOCK
        """
        lexer = FclLexer(InputStream(fcl_text))
        stream = CommonTokenStream(lexer)
        parser = FclParser(stream)
        tree = parser.main()
        listener = FclListenerTester()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

        self.assertEqual(['input_id', 'REAL', '12', '34'], listener.inputs[0])

    def test_var_output(self):
        fcl_text = """
        FUNCTION_BLOCK f_block
            VAR_OUTPUT
                output_id : REAL;
            END_VAR
        END_FUNCTION_BLOCK
        """
        lexer = FclLexer(InputStream(fcl_text))
        stream = CommonTokenStream(lexer)
        parser = FclParser(stream)
        tree = parser.main()
        listener = FclListenerTester()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

        self.assertEqual(['output_id', 'REAL'], listener.outputs[0])

    def test_var_output_range(self):
        fcl_text = """
        FUNCTION_BLOCK f_block
            VAR_OUTPUT
                output_id : REAL; RANGE := ( 12 .. 34 );
            END_VAR
        END_FUNCTION_BLOCK
        """
        lexer = FclLexer(InputStream(fcl_text))
        stream = CommonTokenStream(lexer)
        parser = FclParser(stream)
        tree = parser.main()
        listener = FclListenerTester()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

        self.assertEqual(['output_id', 'REAL', '12', '34'], listener.outputs[0])

    def test_var_input_and_output(self):
        fcl_text = """
        FUNCTION_BLOCK f_block
            VAR_INPUT
                input_id1 : REAL;
            END_VAR
            VAR_OUTPUT
                output_id1 : REAL;
            END_VAR
            VAR_INPUT
                input_id2 : REAL;
            END_VAR
        END_FUNCTION_BLOCK
        """
        lexer = FclLexer(InputStream(fcl_text))
        stream = CommonTokenStream(lexer)
        parser = FclParser(stream)
        tree = parser.main()
        listener = FclListenerTester()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

        self.assertEqual(['output_id1', 'REAL'], listener.outputs[0])
        self.assertEqual(['input_id1', 'REAL'], listener.inputs[0])
        self.assertEqual(['input_id2', 'REAL'], listener.inputs[1])

    def test_fuzzify_block(self):
        fcl_text = """
        FUNCTION_BLOCK f_block
            FUZZIFY fuzzyfy_id
                TERM term1 := mf ;
                TERM term2 := mf ;
            END_FUZZIFY
        END_FUNCTION_BLOCK
        """
        lexer = FclLexer(InputStream(fcl_text))
        stream = CommonTokenStream(lexer)
        parser = FclParser(stream)
        tree = parser.main()
        listener = FclListenerTester()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

        self.assertEqual('fuzzyfy_id', listener.fuzzyfy_blocks[0].get('id'))

        self.assertEqual(2, len(listener.fuzzyfy_blocks[0].get('linguistic_term')))

    def test_linguistic_term(self):
        fcl_text = """
        FUNCTION_BLOCK f_block
            FUZZIFY fuzzyfy_id
                TERM term1 := mf ;
            END_FUZZIFY
        END_FUNCTION_BLOCK
        """
        lexer = FclLexer(InputStream(fcl_text))
        stream = CommonTokenStream(lexer)
        parser = FclParser(stream)
        tree = parser.main()
        listener = FclListenerTester()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        fb = listener.fuzzyfy_blocks[0]
        ling_term = fb.get('linguistic_term')[0]

        self.assertEqual('term1', ling_term.get('id'))

    def test_mf_singleton_id(self):
        fcl_text = """
        FUNCTION_BLOCK f_block
            FUZZIFY fuzzyfy_id
                TERM term1 := mf_id ;
                TERM term2 := mf_id2 ;
            END_FUZZIFY
        END_FUNCTION_BLOCK
        """
        lexer = FclLexer(InputStream(fcl_text))
        stream = CommonTokenStream(lexer)
        parser = FclParser(stream)
        tree = parser.main()
        listener = FclListenerTester()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

        fb = listener.fuzzyfy_blocks[0]
        ling_term = fb.get('linguistic_term')[0]
        ling_term2 = fb.get('linguistic_term')[1]

        self.assertEqual('mf_id', ling_term.get('mf'))
        self.assertEqual('mf_id2', ling_term2.get('mf'))

    def test_mf_singleton_real(self):
        fcl_text = """
        FUNCTION_BLOCK f_block
            FUZZIFY fuzzyfy_id
                TERM term1 := 123 ;
                TERM term2 := 321 ;
            END_FUZZIFY
        END_FUNCTION_BLOCK
        """
        lexer = FclLexer(InputStream(fcl_text))
        stream = CommonTokenStream(lexer)
        parser = FclParser(stream)
        tree = parser.main()
        listener = FclListenerTester()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

        fb = listener.fuzzyfy_blocks[0]
        ling_term = fb.get('linguistic_term')[0]
        ling_term2 = fb.get('linguistic_term')[1]

        self.assertEqual('123', ling_term.get('mf'))
        self.assertEqual('321', ling_term2.get('mf'))

    def test_piece_wise_linear(self):
        fcl_text = """
        FUNCTION_BLOCK f_block
            FUZZIFY fuzzyfy_id
                TERM term1 := (0, 1);
            END_FUZZIFY
        END_FUNCTION_BLOCK
        """
        lexer = FclLexer(InputStream(fcl_text))
        stream = CommonTokenStream(lexer)
        parser = FclParser(stream)
        tree = parser.main()
        listener = FclListenerTester()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

        self.assertEqual([['0', '1']], listener.last_piece_wise_liner)

    def test_piece_wise_linear_more_points(self):
        fcl_text = """
        FUNCTION_BLOCK f_block
            FUZZIFY fuzzyfy_id
                TERM term1 := (0, 1) (1, 2);
            END_FUZZIFY
        END_FUNCTION_BLOCK
        """
        lexer = FclLexer(InputStream(fcl_text))
        stream = CommonTokenStream(lexer)
        parser = FclParser(stream)
        tree = parser.main()
        listener = FclListenerTester()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

        self.assertEqual([['0', '1'], ['1', '2']], listener.last_piece_wise_liner)

    def test_singletons(self):
        fcl_text = """
        FUNCTION_BLOCK f_block
            FUZZIFY fuzzyfy_id
                TERM ipdb := SINGLETONS (0, 1) (1, 2);
            END_FUZZIFY
        END_FUNCTION_BLOCK
        """
        lexer = FclLexer(InputStream(fcl_text))
        stream = CommonTokenStream(lexer)
        parser = FclParser(stream)
        tree = parser.main()
        listener = FclListenerTester()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

        self.assertEqual([['0', '1'], ['1', '2']], listener.last_singletons)

    def test_defuzzify_block_with_range(self):
        fcl_text = """
        FUNCTION_BLOCK f_block
            DEFUZZIFY defuzz_id
                RANGE := ( 12 .. 34 );
            END_DEFUZZIFY
        END_FUNCTION_BLOCK
        """
        lexer = FclLexer(InputStream(fcl_text))
        stream = CommonTokenStream(lexer)
        parser = FclParser(stream)
        tree = parser.main()
        listener = FclListenerTester()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

        self.assertEqual('defuzz_id', listener.last_defuzz.get('id'))
        self.assertEqual(['RANGE:=(12..34);'], listener.last_defuzz.get('items'))

    def test_defuzzify_block_with_default_value_real(self):
        fcl_text = """
        FUNCTION_BLOCK f_block
            DEFUZZIFY defuzz_id
                DEFAULT := 123;
            END_DEFUZZIFY
        END_FUNCTION_BLOCK
        """
        lexer = FclLexer(InputStream(fcl_text))
        stream = CommonTokenStream(lexer)
        parser = FclParser(stream)
        tree = parser.main()
        listener = FclListenerTester()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

        self.assertEqual('defuzz_id', listener.last_defuzz.get('id'))
        self.assertEqual('123', listener.last_default_value)

    def test_defuzzify_block_with_default_value_nc(self):
        fcl_text = """
        FUNCTION_BLOCK f_block
            DEFUZZIFY defuzz_id
                DEFAULT := NC;
            END_DEFUZZIFY
        END_FUNCTION_BLOCK
        """
        lexer = FclLexer(InputStream(fcl_text))
        stream = CommonTokenStream(lexer)
        parser = FclParser(stream)
        tree = parser.main()
        listener = FclListenerTester()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

        self.assertEqual('defuzz_id', listener.last_defuzz.get('id'))
        self.assertEqual('NC', listener.last_default_value)

    def test_defuzzify_block_with_linguistic_term(self):
        fcl_text = """
        FUNCTION_BLOCK f_block
            DEFUZZIFY defuzz_id
                TERM term1 := (0,0) (5,1) (10,0);
                TERM term2 := (1,2);
            END_DEFUZZIFY
        END_FUNCTION_BLOCK
        """
        lexer = FclLexer(InputStream(fcl_text))
        stream = CommonTokenStream(lexer)
        parser = FclParser(stream)
        tree = parser.main()
        listener = FclListenerTester()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

        self.assertEqual('defuzz_id', listener.last_defuzz.get('id'))
        self.assertEqual('term1', listener.last_linguistic_terms[0].get('id'))
        self.assertEqual([['1', '2']], listener.last_piece_wise_liner)
        self.assertEqual('term2', listener.last_linguistic_terms[1].get('id'))
