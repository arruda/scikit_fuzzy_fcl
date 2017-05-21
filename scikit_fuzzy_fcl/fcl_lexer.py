# -*- coding: utf-8 -*-
from __future__ import absolute_import
import sys
if sys.version_info >= (3, 0):  # pragma: no cover
    from .py3_parser.FclLexer import *  # noqa: F403,F401
else:  # pragma: no cover
    from .py2_parser.FclLexer import *  # noqa: F403,F401
