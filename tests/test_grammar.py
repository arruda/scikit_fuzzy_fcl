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
        self.accumulation_methods = []
        self.rules = []
        self.conditions = []

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

    def exitDefuzzification_method(self, ctx):
        self.last_deffuz_method = ctx.getChild(2).getText()

    def exitRule_block(self, ctx):
        rule_items = ctx.rule_item()
        if rule_items:
            rule_items = [i.getText() for i in ctx.rule_item()]
        rule_block = {
            'id': ctx.ID().getText(),
            'rule_items': rule_items
        }
        self.last_rule_block = rule_block

    def exitOperator_definition(self, ctx):
        op_def = ctx.getChild(0)
        self.last_op_def = {
            'type': op_def.getChild(0).getText(),
            'def': op_def.getChild(2).getText()
        }

    def exitActivation_method(self, ctx):
        activation = ctx.PROD() or ctx.MIN()
        self.last_activation_method = activation.getText()

    def exitAccumulation_method(self, ctx):
        accumulation = ctx.MAX() or ctx.BSUM() or ctx.NSUM() or ctx.PROBOR() or ctx.SUM()
        self.accumulation_methods.append(accumulation.getText())

    def exitRule_def(self, ctx):
        self.rules.append({
            'id': ctx.rule_name().getText()
        })

    def exitCondition(self, ctx):
        condition = {
            'head': ctx.getChild(0).getText()
        }
        self.conditions.append(
            condition
        )


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
                TERM sing := SINGLETONS (0, 1) (1, 2);
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

    def test_defuzzify_block_with_defuzzification_method(self):
        fcl_text = """
        FUNCTION_BLOCK f_block
            DEFUZZIFY defuzz_id
                METHOD : COG;
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

        self.assertEqual('COG', listener.last_deffuz_method)

    def test_rule_block(self):
        fcl_text = """
        FUNCTION_BLOCK f_block
            RULEBLOCK rule1
            END_RULEBLOCK
        END_FUNCTION_BLOCK
        """
        lexer = FclLexer(InputStream(fcl_text))
        stream = CommonTokenStream(lexer)
        parser = FclParser(stream)
        tree = parser.main()
        listener = FclListenerTester()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

        self.assertEqual('rule1', listener.last_rule_block.get('id'))

    def test_rule_block_rule_item_or(self):
        fcl_text = """
        FUNCTION_BLOCK f_block
            RULEBLOCK rule1
                OR : MAX;
            END_RULEBLOCK
        END_FUNCTION_BLOCK
        """
        lexer = FclLexer(InputStream(fcl_text))
        stream = CommonTokenStream(lexer)
        parser = FclParser(stream)
        tree = parser.main()
        listener = FclListenerTester()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

        self.assertEqual('rule1', listener.last_rule_block.get('id'))
        self.assertEqual('OR', listener.last_op_def.get('type'))
        self.assertEqual('MAX', listener.last_op_def.get('def'))

    def test_rule_block_rule_item_and(self):
        fcl_text = """
        FUNCTION_BLOCK f_block
            RULEBLOCK rule1
                AND : MIN;
            END_RULEBLOCK
        END_FUNCTION_BLOCK
        """
        lexer = FclLexer(InputStream(fcl_text))
        stream = CommonTokenStream(lexer)
        parser = FclParser(stream)
        tree = parser.main()
        listener = FclListenerTester()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

        self.assertEqual('rule1', listener.last_rule_block.get('id'))
        self.assertEqual('AND', listener.last_op_def.get('type'))
        self.assertEqual('MIN', listener.last_op_def.get('def'))

    def test_rule_block_rule_item_activation_method(self):
        fcl_text = """
        FUNCTION_BLOCK f_block
            RULEBLOCK rule1
                ACT : MIN;
            END_RULEBLOCK
        END_FUNCTION_BLOCK
        """
        lexer = FclLexer(InputStream(fcl_text))
        stream = CommonTokenStream(lexer)
        parser = FclParser(stream)
        tree = parser.main()
        listener = FclListenerTester()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

        self.assertEqual('rule1', listener.last_rule_block.get('id'))
        self.assertEqual('MIN', listener.last_activation_method)

    def test_rule(self):
        fcl_text = """
        FUNCTION_BLOCK f_block
            RULEBLOCK rule1
                RULE first_rule : IF something THEN finalthing IS conclusion;
                RULE 2 : IF something THEN finalthing IS conclusion;
            END_RULEBLOCK
        END_FUNCTION_BLOCK
        """
        # RULE first_rule : IF something IS otherthing OR something2 IS otherthing2 THEN finalthing IS conclusion;
        lexer = FclLexer(InputStream(fcl_text))
        stream = CommonTokenStream(lexer)
        parser = FclParser(stream)
        tree = parser.main()
        listener = FclListenerTester()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        self.assertEqual('first_rule', listener.rules[0].get('id'))
        self.assertEqual('2', listener.rules[1].get('id'))

    def test_rule_if_clause_condition_simple_if_clause(self):
        fcl_text = """
        FUNCTION_BLOCK f_block
            RULEBLOCK rule1
                RULE first_rule : IF something THEN conclusion IS final;
            END_RULEBLOCK
        END_FUNCTION_BLOCK
        """

        class FclListenerRules(FclListener):
            def enterIf_clause(_self, ctx):
                condition = ctx.condition().getText()
                self.assertEqual(condition, 'something')

        lexer = FclLexer(InputStream(fcl_text))
        stream = CommonTokenStream(lexer)
        parser = FclParser(stream)
        tree = parser.main()

        listener = FclListenerRules()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

    def test_rule_if_clause_condition_if_clause_with_and(self):
        fcl_text = """
        FUNCTION_BLOCK f_block
            RULEBLOCK rule1
                RULE first_rule : IF something AND otherthing THEN conclusion IS final;
            END_RULEBLOCK
        END_FUNCTION_BLOCK
        """

        class FclListenerRules(FclListener):
            def enterIf_clause(_self, ctx):
                condition = ctx.condition()
                something = condition.getChild(0).getText()
                operator = condition.getChild(1).getText()
                otherthing = condition.getChild(2).getText()
                self.assertEqual(something, 'something')
                self.assertEqual(operator, 'AND')
                self.assertEqual(otherthing, 'otherthing')

        lexer = FclLexer(InputStream(fcl_text))
        stream = CommonTokenStream(lexer)
        parser = FclParser(stream)
        tree = parser.main()

        listener = FclListenerRules()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

    def test_rule_if_clause_condition_then_clause(self):
        fcl_text = """
        FUNCTION_BLOCK f_block
            RULEBLOCK rule1
                RULE first_rule : IF something AND otherthing THEN final IS final2;
            END_RULEBLOCK
        END_FUNCTION_BLOCK
        """

        class FclListenerRules(FclListener):
            def enterThen_clause(_self, ctx):
                conclusion = ctx.conclusion()
                subconclusion = conclusion.sub_conclusion()[0]
                final = subconclusion.ID()[0].getText()
                final2 = subconclusion.ID()[1].getText()
                self.assertEqual(final, 'final')
                self.assertEqual(final2, 'final2')

        lexer = FclLexer(InputStream(fcl_text))
        stream = CommonTokenStream(lexer)
        parser = FclParser(stream)
        tree = parser.main()

        listener = FclListenerRules()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

    def test_rule_if_clause_condition_then_clause_many_sub_conclusions(self):
        fcl_text = """
        FUNCTION_BLOCK f_block
            RULEBLOCK rule1
                RULE first_rule : IF something AND otherthing THEN final IS final2, final3 IS final4;
            END_RULEBLOCK
        END_FUNCTION_BLOCK
        """

        class FclListenerRules(FclListener):
            def enterThen_clause(_self, ctx):
                conclusion = ctx.conclusion()
                subconclusions = conclusion.sub_conclusion()
                final = subconclusions[0].ID()[0].getText()
                final2 = subconclusions[0].ID()[1].getText()
                final3 = subconclusions[1].ID()[0].getText()
                final4 = subconclusions[1].ID()[1].getText()
                self.assertEqual(final, 'final')
                self.assertEqual(final2, 'final2')
                self.assertEqual(final3, 'final3')
                self.assertEqual(final4, 'final4')

        lexer = FclLexer(InputStream(fcl_text))
        stream = CommonTokenStream(lexer)
        parser = FclParser(stream)
        tree = parser.main()

        listener = FclListenerRules()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

    def test_rule_if_clause_condition_then_clause_with_x(self):
        fcl_text = """
        FUNCTION_BLOCK f_block
            RULEBLOCK rule1
                RULE first_rule : IF something AND otherthing THEN final IS final2 WITH 123;
            END_RULEBLOCK
        END_FUNCTION_BLOCK
        """

        class FclListenerRules(FclListener):
            def enterThen_clause(_self, ctx):
                conclusion = ctx.conclusion()
                subconclusion = conclusion.sub_conclusion()[0]
                final = subconclusion.ID()[0].getText()
                final2 = subconclusion.ID()[1].getText()
                self.assertEqual(final, 'final')
                self.assertEqual(final2, 'final2')

            def enterWith_x(_self, ctx):
                real = ctx.REAL().getText()

                self.assertEqual(real, '123')

        lexer = FclLexer(InputStream(fcl_text))
        stream = CommonTokenStream(lexer)
        parser = FclParser(stream)
        tree = parser.main()

        listener = FclListenerRules()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

    def test_sub_condition_not(self):
        fcl_text = """
        FUNCTION_BLOCK f_block
            RULEBLOCK rule1
                RULE first_rule : IF NOT something THEN final IS final2;
            END_RULEBLOCK
        END_FUNCTION_BLOCK
        """

        class FclListenerRules(FclListener):
            def enterSubcondition(_self, ctx):
                has_not = ctx.NOT() is not None
                sub_bare = ctx.subcondition_bare().getText()
                self.assertEqual(has_not, True)
                self.assertEqual(sub_bare, 'something')

        lexer = FclLexer(InputStream(fcl_text))
        stream = CommonTokenStream(lexer)
        parser = FclParser(stream)
        tree = parser.main()

        listener = FclListenerRules()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

    def test_subcondition_bare_is(self):
        fcl_text = """
        FUNCTION_BLOCK f_block
            RULEBLOCK rule1
                RULE first_rule : IF something IS otherthing THEN final IS final2;
            END_RULEBLOCK
        END_FUNCTION_BLOCK
        """

        class FclListenerRules(FclListener):
            def enterSubcondition_bare(_self, ctx):
                ids = [i.getText() for i in ctx.ID()]
                is_negated = ctx.NOT() is not None
                self.assertEqual(ids, ['something', 'otherthing'])
                self.assertEqual(is_negated, False)

        lexer = FclLexer(InputStream(fcl_text))
        stream = CommonTokenStream(lexer)
        parser = FclParser(stream)
        tree = parser.main()

        listener = FclListenerRules()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

    def test_subcondition_bare_is_negated(self):
        fcl_text = """
        FUNCTION_BLOCK f_block
            RULEBLOCK rule1
                RULE first_rule : IF something IS NOT otherthing THEN final IS final2;
            END_RULEBLOCK
        END_FUNCTION_BLOCK
        """

        class FclListenerRules(FclListener):
            def enterSubcondition_bare(_self, ctx):
                ids = [i.getText() for i in ctx.ID()]
                is_negated = ctx.NOT() is not None
                self.assertEqual(ids, ['something', 'otherthing'])
                self.assertEqual(is_negated, True)

        lexer = FclLexer(InputStream(fcl_text))
        stream = CommonTokenStream(lexer)
        parser = FclParser(stream)
        tree = parser.main()

        listener = FclListenerRules()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

    def test_subcondition_paren(self):
        fcl_text = """
        FUNCTION_BLOCK f_block
            RULEBLOCK rule1
                RULE first_rule : IF (something)  THEN final IS final2;
            END_RULEBLOCK
        END_FUNCTION_BLOCK
        """

        class FclListenerRules(FclListener):
            def enterSubcondition_paren(_self, ctx):
                condition = ctx.condition().getText()
                self.assertEqual(condition, 'something')

        lexer = FclLexer(InputStream(fcl_text))
        stream = CommonTokenStream(lexer)
        parser = FclParser(stream)
        tree = parser.main()

        listener = FclListenerRules()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

    def test_subcondition_paren_complex(self):
        fcl_text = """
        FUNCTION_BLOCK f_block
            RULEBLOCK rule1
                RULE first_rule : IF (something IS NOT otherthing)  THEN final IS final2;
            END_RULEBLOCK
        END_FUNCTION_BLOCK
        """

        class FclListenerRules(FclListener):
            def enterSubcondition_paren(_self, ctx):
                condition = ctx.condition().getText()
                self.assertEqual(condition, 'somethingISNOTotherthing')

        lexer = FclLexer(InputStream(fcl_text))
        stream = CommonTokenStream(lexer)
        parser = FclParser(stream)
        tree = parser.main()

        listener = FclListenerRules()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

    def test_if_clause_complex(self):
        fcl_text = """
        FUNCTION_BLOCK f_block
            RULEBLOCK rule1
                RULE first_rule : IF (something IS NOT otherthing) THEN final IS final2;
            END_RULEBLOCK
        END_FUNCTION_BLOCK
        """

        class FclListenerRules(FclListener):
            def enterSubcondition_paren(_self, ctx):
                condition = ctx.condition().getText()
                self.assertEqual(condition, 'somethingISNOTotherthing')

        lexer = FclLexer(InputStream(fcl_text))
        stream = CommonTokenStream(lexer)
        parser = FclParser(stream)
        tree = parser.main()

        listener = FclListenerRules()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
