# -*- coding: utf-8 -*-
from unittest import TestCase

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

    # def test_should_create_empyt_control_system_if_no_declaration(self):
    #     fcl_text = """
    #     FUNCTION_BLOCK my_system
    #     END_FUNCTION_BLOCK
    #     """
    #     lexer = FclLexer(InputStream(fcl_text))
    #     stream = CommonTokenStream(lexer)
    #     parser = FclParser(stream)
    #     tree = parser.main()

    #     listener = ScikitFuzzyFclListener()
    #     walker = ParseTreeWalker()
    #     walker.walk(listener, tree)
    #     control_system = listener.control_system
    #     self.assertIsNot(control_system, None)
