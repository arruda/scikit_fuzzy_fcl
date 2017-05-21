# -*- coding: utf-8 -*-
from __future__ import absolute_import

# import numpy as np
# from skfuzzy.control.controlsystem import ControlSystem
# from skfuzzy.control.antecedent_consequent import Antecedent  # , Consequent

from antlr4 import InputStream, ParseTreeWalker  # ,FileStream
from antlr4.CommonTokenStream import CommonTokenStream

from .FclLexer import FclLexer
from .FclParser import FclParser
from .FclListener import FclListener


class ScikitFuzzyFclListener(FclListener):
    """
    FclListener responsable of transforming the parsed Fcl file
    into corresponding scikit-fuzzy objects
    """
    def __init__(self):
        super(ScikitFuzzyFclListener, self).__init__()
        self.control_system = None

    # def visitErrorNode(self, node):
    #     raise Exception()


class FclLoader(object):
    """
        This class will wrap all the objects necessary to transform a fcl text (string) into
        the corresponding scikit-fuzzy control-system.

        To use this class, one should just instantiate it, and then call the `load` method.
        this will return the scikit-fuzzy objects representing what was parsed from the fcl text
    """
    def __init__(self, fcl_text):
        super(FclLoader, self).__init__()
        self.fcl_text = fcl_text
        self.lexer = None

    def load_lexer(self):
        self.lexer = FclLexer(InputStream(self.fcl_text))

    def load_listener(self):
        self.listener = ScikitFuzzyFclListener()

    def load_stream(self):
        self.steam = CommonTokenStream(self.lexer)

    def load_parser(self):
        self.parser = FclParser(self.stream)

    def run_tree_walker(self):
        tree = self.parser.main()
        walker = ParseTreeWalker()
        walker.walk(self.listener, tree)

    def load(self):
        self.load_lexer()
        self.load_listener()
        self.load_stream()
        self.load_parser()
        self.run_tree_walker()
        return self.listener.control_system
