# -*- coding: utf-8 -*-
from __future__ import absolute_import
import sys
if sys.version_info >= (3, 0):
    from .py3_parser.FclParser import *
else:
    from .py2_parser.FclParser import *
