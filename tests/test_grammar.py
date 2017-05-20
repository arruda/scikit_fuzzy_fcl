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

    def enterMain(self, ctx):
        pass

    def exitMain(self, ctx):
        pass

    def enterFcl(self, ctx):
        pass

    def exitFcl(self, ctx):
        pass

    def enterFunction_block(self, ctx):
        self.function_blocks_ids.append(ctx.ID().getText())

    def exitFunction_block(self, ctx):
        pass


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
