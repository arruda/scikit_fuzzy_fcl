# -*- coding: utf-8 -*-
from unittest import TestCase

from unipath import Path
from mock import patch

from antlr4 import InputStream, ParseTreeWalker
from antlr4.CommonTokenStream import CommonTokenStream

from scikit_fuzzy_fcl.FclListener import ScikitFuzzyFclListener
from scikit_fuzzy_fcl.FclLexer import FclLexer
from scikit_fuzzy_fcl.FclParser import FclParser, FclParserException


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
