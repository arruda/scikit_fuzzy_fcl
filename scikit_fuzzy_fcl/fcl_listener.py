# -*- coding: utf-8 -*-
from __future__ import absolute_import
import sys
from skfuzzy.control.controlsystem import ControlSystem

from .fcl_parser import FclParserException

if sys.version_info >= (3, 0):  # pragma: no cover
    from .py3_parser.FclListener import FclListener  # noqa: F403,F401
else:  # pragma: no cover
    from .py2_parser.FclListener import FclListener  # noqa: F403,F401

# import numpy as np
# from skfuzzy.control.antecedent_consequent import Antecedent  # , Consequent


class ScikitFuzzyFclListener(FclListener):
    """
    FclListener responsable for transforming the parsed Fcl file
    into corresponding scikit-fuzzy objects
    """
    def __init__(self):
        super(ScikitFuzzyFclListener, self).__init__()
        self.control_system = None

    def visitErrorNode(self, node):
        raise FclParserException(node)

    def enterFunction_block(self, ctx):
        self.control_system = ControlSystem()
