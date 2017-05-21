# -*- coding: utf-8 -*-
from unittest import TestCase
from collections import namedtuple
from unipath import Path
from mock import Mock, MagicMock, patch

from scikit_fuzzy_fcl.loader import FclLoader


TESTS_DIR = Path(__file__).ancestor(1)
FIXTURES_DIR = TESTS_DIR.child('fixtures')


class TestFclLoader(TestCase):

    @patch('scikit_fuzzy_fcl.loader.FclLoader.load_lexer')
    @patch('scikit_fuzzy_fcl.loader.FclLoader.load_listener')
    @patch('scikit_fuzzy_fcl.loader.FclLoader.load_stream')
    @patch('scikit_fuzzy_fcl.loader.FclLoader.load_parser')
    @patch('scikit_fuzzy_fcl.loader.FclLoader.run_tree_walker')
    def test_load_should_return_listener_control_system(self, run_tree, l_parser, l_stream, l_listener, l_lexer):
        fcl_loader = FclLoader('fcl_text')
        fake_listener = namedtuple('Listener', 'control_system')
        fake_listener.control_system = "control_system"
        fcl_loader.listener = fake_listener
        control_system = fcl_loader.load()

        self.assertEqual(control_system, "control_system")
