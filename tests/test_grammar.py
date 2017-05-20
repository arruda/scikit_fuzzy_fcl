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
        self.last_var_def = None

    def enterFunction_block(self, ctx):
        f_id = ctx.ID()
        if f_id:
            self.function_blocks_ids.append(ctx.ID().getText())

    def exitVar_input(self, ctx):
        if self.last_var_def:
            self.inputs.append(self.last_var_def)

    # Exit a parse tree produced by FclParser#var_output.
    def exitVar_output(self, ctx):
        if self.last_var_def:
            self.outputs.append(self.last_var_def)
        pass

    def enterVar_def(self, ctx):
        self.last_var_def = [ctx.ID().getText(), ctx.data_type().getText()]
        vrange = ctx.vrange()
        if vrange:
            self.last_var_def.extend(real.getText() for real in vrange.REAL())


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
