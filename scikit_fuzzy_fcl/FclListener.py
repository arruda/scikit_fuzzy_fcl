# -*- coding: utf-8 -*-
from __future__ import absolute_import
import sys
if sys.version_info >= (3, 0):
    from .py3_parser.FclListener import *
else:
    from .py2_parser.FclListener import *
