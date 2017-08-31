# -*- coding: utf-8 -*-
from unittest import TestCase
import numpy as np

from unipath import Path
from mock import patch

from antlr4 import InputStream, ParseTreeWalker
from antlr4.CommonTokenStream import CommonTokenStream

from scikit_fuzzy_fcl.fcl_listener import ScikitFuzzyFclListener
from scikit_fuzzy_fcl.fcl_lexer import FclLexer
from scikit_fuzzy_fcl.fcl_parser import FclParser, FclParserException


TESTS_DIR = Path(__file__).ancestor(1)
FIXTURES_DIR = TESTS_DIR.child('fixtures')


class TestScikitFuzzyFclListener(TestCase):

    def test_should_raise_parser_exception_if_incorrect_fcl_text(self):
        fcl_text = "INCORRECT FCL TEXT"
        lexer = FclLexer(InputStream(fcl_text))
        stream = CommonTokenStream(lexer)
        parser = FclParser(stream)
        tree = parser.main()

        listener = ScikitFuzzyFclListener()
        walker = ParseTreeWalker()
        with self.assertRaises(FclParserException):
            walker.walk(listener, tree)

    def test_should_create_empyt_control_system_if_no_declaration(self):
        fcl_text = """
        FUNCTION_BLOCK my_system
        END_FUNCTION_BLOCK
        """
        lexer = FclLexer(InputStream(fcl_text))
        stream = CommonTokenStream(lexer)
        parser = FclParser(stream)
        tree = parser.main()

        listener = ScikitFuzzyFclListener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        control_system = listener.control_system
        self.assertIsNot(control_system, None)

    def test_var_inputs_if_var_input_empty(self):
        fcl_text = """
        FUNCTION_BLOCK my_system
            VAR_INPUT
            END_VAR
        END_FUNCTION_BLOCK
        """
        lexer = FclLexer(InputStream(fcl_text))
        stream = CommonTokenStream(lexer)
        parser = FclParser(stream)
        tree = parser.main()

        listener = ScikitFuzzyFclListener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        loaded_vars = listener.vars
        self.assertEqual(loaded_vars, {})

    def test_add_vars_if_var_input_simple(self):
        fcl_text = """
        FUNCTION_BLOCK my_system
            VAR_INPUT
                var1 : REAL;
            END_VAR
        END_FUNCTION_BLOCK
        """
        lexer = FclLexer(InputStream(fcl_text))
        stream = CommonTokenStream(lexer)
        parser = FclParser(stream)
        tree = parser.main()

        listener = ScikitFuzzyFclListener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        loaded_vars = listener.vars
        self.assertEqual(loaded_vars, {'var1': {'type': 'REAL', 'range': None}})

    def test_antecedents_created_when_fuzzify_block_described(self):
        fcl_text = """
        FUNCTION_BLOCK my_system
            FUZZIFY antecedent1
            END_FUZZIFY
        END_FUNCTION_BLOCK
        """
        lexer = FclLexer(InputStream(fcl_text))
        stream = CommonTokenStream(lexer)
        parser = FclParser(stream)
        tree = parser.main()

        listener = ScikitFuzzyFclListener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        antecedents = listener.antecedents
        self.assertIn('antecedent1', antecedents)
        self.assertEqual('antecedent1', antecedents.get('antecedent1').get('value').label)

    def test_antecedents_define_universe_if_range_defined_in_var(self):
        fcl_text = """
        FUNCTION_BLOCK my_system
            VAR_INPUT
                antecedent1 : REAL (1 .. 9);
            END_VAR
            FUZZIFY antecedent1
            END_FUZZIFY
        END_FUNCTION_BLOCK
        """
        lexer = FclLexer(InputStream(fcl_text))
        stream = CommonTokenStream(lexer)
        parser = FclParser(stream)
        tree = parser.main()

        listener = ScikitFuzzyFclListener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        antecedents = listener.antecedents
        expected_universe = np.asarray([1., 9.])
        self.assertIn('antecedent1', antecedents)
        self.assertEqual('antecedent1', antecedents.get('antecedent1').get('value').label)
        np.testing.assert_array_equal(expected_universe, antecedents.get('antecedent1').get('value').universe)

    def test_antecedents_term_defined_if_present(self):
        fcl_text = """
        FUNCTION_BLOCK my_system
            FUZZIFY antecedent1
                TERM mf1 := (0, 1) (1, 1);
            END_FUZZIFY
        END_FUNCTION_BLOCK
        """
        lexer = FclLexer(InputStream(fcl_text))
        stream = CommonTokenStream(lexer)
        parser = FclParser(stream)
        tree = parser.main()

        listener = ScikitFuzzyFclListener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        antecedents = listener.antecedents
        self.assertIn('antecedent1', antecedents)
        self.assertEqual('antecedent1', antecedents.get('antecedent1').get('value').label)
        self.assertIn('mf1', antecedents.get('antecedent1').get('value').terms)
        self.assertIn('mf1', antecedents.get('antecedent1').get('value').terms.get('mf1').label)

    def test_antecedents_term_has_correct_mf_value(self):
        fcl_text = """
        FUNCTION_BLOCK my_system
            FUZZIFY antecedent1
                TERM mf1 := (0, 1) (0.5, 0);
            END_FUZZIFY
        END_FUNCTION_BLOCK
        """
        lexer = FclLexer(InputStream(fcl_text))
        stream = CommonTokenStream(lexer)
        parser = FclParser(stream)
        tree = parser.main()

        listener = ScikitFuzzyFclListener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        antecedent = listener.antecedents.get('antecedent1').get('value')
        term = antecedent['mf1']
        expected_mf_value = np.asarray([1, 0])
        np.testing.assert_array_equal(expected_mf_value, term.mf)

    def test_antecedents_universe_has_correct_value_based_on_term(self):
        fcl_text = """
        FUNCTION_BLOCK my_system
            FUZZIFY antecedent1
                TERM mf1 := (0, 1) (0.5, 0);
            END_FUZZIFY
        END_FUNCTION_BLOCK
        """
        lexer = FclLexer(InputStream(fcl_text))
        stream = CommonTokenStream(lexer)
        parser = FclParser(stream)
        tree = parser.main()

        listener = ScikitFuzzyFclListener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        antecedent = listener.antecedents.get('antecedent1').get('value')
        expected_universe = np.asarray([0, 0.5])
        np.testing.assert_array_equal(expected_universe, antecedent.universe)

    def test_antecedents_universe_has_correct_value_based_on_more_then_one_term(self):
        fcl_text = """
        FUNCTION_BLOCK my_system
            FUZZIFY antecedent1
                TERM mf1 := (0, 1) (0.5, 0);
                TERM mf2 := (1, 0.3) (2, 0) (3, 1);
            END_FUZZIFY
        END_FUNCTION_BLOCK
        """
        lexer = FclLexer(InputStream(fcl_text))
        stream = CommonTokenStream(lexer)
        parser = FclParser(stream)
        tree = parser.main()

        listener = ScikitFuzzyFclListener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        antecedent = listener.antecedents.get('antecedent1').get('value')
        expected_universe = np.asarray([0., 0.5, 1., 2., 3])
        np.testing.assert_array_equal(expected_universe, antecedent.universe)

    def test_antecedents_terms_have_correct_mf_values_with_more_then_one_term(self):
        fcl_text = """
        FUNCTION_BLOCK my_system
            FUZZIFY antecedent1
                TERM mf1 := (0, 1) (0.5, 0);
                TERM mf2 := (1, 0.3) (2, 0) (3, 1);
                TERM mf3 := (2, 0.4) (4, 1) (5, 1);
            END_FUZZIFY
        END_FUNCTION_BLOCK
        """
        lexer = FclLexer(InputStream(fcl_text))
        stream = CommonTokenStream(lexer)
        parser = FclParser(stream)
        tree = parser.main()

        listener = ScikitFuzzyFclListener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        antecedent = listener.antecedents.get('antecedent1').get('value')
        term = antecedent['mf1']
        expected_mf_value = np.asarray([1, 0, 0, 0, 0, 0, 0])
        np.testing.assert_array_equal(expected_mf_value, term.mf)

        term2 = antecedent['mf2']
        expected_mf_value = np.asarray([0, 0, 0.3, 0, 1, 0, 0])
        np.testing.assert_array_equal(expected_mf_value, term2.mf)

        term3 = antecedent['mf3']
        expected_mf_value = np.asarray([0, 0, 0, 0.4, 0.7, 1, 1])
        np.testing.assert_array_equal(expected_mf_value, term3.mf)

    def test_antecedents_universe_have_correct_values_using_singleton(self):
        fcl_text = """
        FUNCTION_BLOCK my_system
            FUZZIFY antecedent1
                TERM mf1 := 1.0;
                TERM mf2 := 3.0;
            END_FUZZIFY
        END_FUNCTION_BLOCK
        """
        lexer = FclLexer(InputStream(fcl_text))
        stream = CommonTokenStream(lexer)
        parser = FclParser(stream)
        tree = parser.main()

        listener = ScikitFuzzyFclListener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        antecedent = listener.antecedents.get('antecedent1').get('value')
        expected_universe_value = np.asarray([1., 3.])
        np.testing.assert_array_equal(expected_universe_value, antecedent.universe)

    def test_antecedents_terms_have_correct_mf_values_using_singleton(self):
        fcl_text = """
        FUNCTION_BLOCK my_system
            FUZZIFY antecedent1
                TERM mf1 := 1.0;
            END_FUZZIFY
        END_FUNCTION_BLOCK
        """
        lexer = FclLexer(InputStream(fcl_text))
        stream = CommonTokenStream(lexer)
        parser = FclParser(stream)
        tree = parser.main()

        listener = ScikitFuzzyFclListener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        antecedent = listener.antecedents.get('antecedent1').get('value')
        term = antecedent['mf1']
        expected_mf_value = np.asarray([1])
        np.testing.assert_array_equal(expected_mf_value, term.mf)

    def test_antecedents_terms_have_correct_mf_values_using_many_singleton(self):
        fcl_text = """
        FUNCTION_BLOCK my_system
            FUZZIFY antecedent1
                TERM mf1 := 3.0;
                TERM mf2 := 2.0;
                TERM mf3 := 1.0;
            END_FUZZIFY
        END_FUNCTION_BLOCK
        """
        lexer = FclLexer(InputStream(fcl_text))
        stream = CommonTokenStream(lexer)
        parser = FclParser(stream)
        tree = parser.main()

        listener = ScikitFuzzyFclListener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        antecedent = listener.antecedents.get('antecedent1').get('value')
        term = antecedent['mf1']
        expected_mf_value = np.asarray([0, 0, 1])
        np.testing.assert_array_equal(expected_mf_value, term.mf)

        term = antecedent['mf2']
        expected_mf_value = np.asarray([0, 1, 0])
        np.testing.assert_array_equal(expected_mf_value, term.mf)

        term = antecedent['mf3']
        expected_mf_value = np.asarray([1, 0, 0])
        np.testing.assert_array_equal(expected_mf_value, term.mf)

    def test_antecedents_terms_have_correct_mf_values_using_singleton_and_piecewise(self):
        fcl_text = """
        FUNCTION_BLOCK my_system
            FUZZIFY antecedent1
                TERM mf1 := 4.0;
                TERM mf2 := (0, 0.2) (2, 0) (3, 1);
                TERM mf3 := 1.0;
            END_FUZZIFY
        END_FUNCTION_BLOCK
        """
        lexer = FclLexer(InputStream(fcl_text))
        stream = CommonTokenStream(lexer)
        parser = FclParser(stream)
        tree = parser.main()

        listener = ScikitFuzzyFclListener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        antecedent = listener.antecedents.get('antecedent1').get('value')
        term = antecedent['mf1']
        expected_mf_value = np.asarray([0, 0, 0, 0, 1])  # fx[0], fx[1], fx[2], fx[3], f[4]
        np.testing.assert_array_equal(expected_mf_value, term.mf)

        term = antecedent['mf2']
        expected_mf_value = np.asarray([0.2, 0.1, 0, 1, 0])  # fx[0], fx[1], fx[2], fx[3], f[4]
        np.testing.assert_array_equal(expected_mf_value, term.mf)

        term = antecedent['mf3']
        expected_mf_value = np.asarray([0, 1, 0, 0, 0])  # fx[0], fx[1], fx[2], fx[3], f[4]
        np.testing.assert_array_equal(expected_mf_value, term.mf)

    def test_consequents_created_when_defuzzify_block_described(self):
        fcl_text = """
        FUNCTION_BLOCK my_system
            DEFUZZIFY consequent1
            END_DEFUZZIFY
        END_FUNCTION_BLOCK
        """
        lexer = FclLexer(InputStream(fcl_text))
        stream = CommonTokenStream(lexer)
        parser = FclParser(stream)
        tree = parser.main()

        listener = ScikitFuzzyFclListener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        consequents = listener.consequents
        self.assertIn('consequent1', consequents)
        self.assertEqual('consequent1', consequents.get('consequent1').get('value').label)

    def test_consequent_define_universe_if_range_defined_in_var(self):
        fcl_text = """
        FUNCTION_BLOCK my_system
            VAR_output
                consequent1 : REAL (1 .. 9);
            END_VAR
            DEFUZZIFY consequent1
            END_DEFUZZIFY
        END_FUNCTION_BLOCK
        """
        lexer = FclLexer(InputStream(fcl_text))
        stream = CommonTokenStream(lexer)
        parser = FclParser(stream)
        tree = parser.main()

        listener = ScikitFuzzyFclListener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        listener = ScikitFuzzyFclListener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        consequents = listener.consequents
        expected_universe = np.asarray([1., 9.])
        self.assertIn('consequent1', consequents)
        self.assertEqual('consequent1', consequents.get('consequent1').get('value').label)
        np.testing.assert_array_equal(expected_universe, consequents.get('consequent1').get('value').universe)

    def test_consequent_define_universe_override_range_defined_in_var_if_defined_in_consequent(self):
        fcl_text = """
        FUNCTION_BLOCK my_system
            VAR_output
                consequent1 : REAL (1 .. 9);
            END_VAR
            DEFUZZIFY consequent1
                RANGE := (0 .. 30);
            END_DEFUZZIFY
        END_FUNCTION_BLOCK
        """
        lexer = FclLexer(InputStream(fcl_text))
        stream = CommonTokenStream(lexer)
        parser = FclParser(stream)
        tree = parser.main()

        listener = ScikitFuzzyFclListener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        listener = ScikitFuzzyFclListener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        consequents = listener.consequents
        expected_universe = np.asarray([0., 30.])
        self.assertIn('consequent1', consequents)
        self.assertEqual('consequent1', consequents.get('consequent1').get('value').label)
        np.testing.assert_array_equal(expected_universe, consequents.get('consequent1').get('value').universe)

    def test_consequents_term_defined_if_present(self):
        fcl_text = """
        FUNCTION_BLOCK my_system
            DEFUZZIFY consequent1
                TERM mf1 := (0, 1) (1, 1);
            END_DEFUZZIFY
        END_FUNCTION_BLOCK
        """
        lexer = FclLexer(InputStream(fcl_text))
        stream = CommonTokenStream(lexer)
        parser = FclParser(stream)
        tree = parser.main()

        listener = ScikitFuzzyFclListener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        consequents = listener.consequents
        self.assertIn('consequent1', consequents)
        self.assertEqual('consequent1', consequents.get('consequent1').get('value').label)
        self.assertIn('mf1', consequents.get('consequent1').get('value').terms)
        self.assertIn('mf1', consequents.get('consequent1').get('value').terms.get('mf1').label)
