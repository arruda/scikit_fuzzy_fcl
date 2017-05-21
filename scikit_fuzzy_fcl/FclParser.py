# -*- coding: utf-8 -*-
from __future__ import absolute_import
import sys
if sys.version_info >= (3, 0):  # pragma: no cover
    from .py3_parser.FclParser import *
else:  # pragma: no cover
    from .py2_parser.FclParser import *


class FclParserException(RuntimeError):
    """
    Exception raised by any error during the parse of the FCL file
    """
    def __init__(self, node):
        payload = node.getPayload()
        symbol = node.getText()
        message = "Error parsing FCL. '{}' is not valid in the line {}:{}.".format(
            symbol,
            payload.line,
            payload.column
        )
        self.message = message
        self.node = node
        super(FclParserException, self).__init__(message)
