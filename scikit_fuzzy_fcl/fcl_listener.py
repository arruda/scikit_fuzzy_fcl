# -*- coding: utf-8 -*-
from __future__ import absolute_import, division
from collections import OrderedDict
import sys

import numpy as np
from skfuzzy.control.controlsystem import ControlSystem
from skfuzzy.control.antecedent_consequent import Antecedent

from .fcl_parser import FclParserException

if sys.version_info >= (3, 0):  # pragma: no cover
    from .py3_parser.FclListener import FclListener  # noqa: F403,F401
else:  # pragma: no cover
    from .py2_parser.FclListener import FclListener  # noqa: F403,F401

try:
    xrange
except NameError:  # python3
    xrange = range


def handle_piecewise_function(universe, x_values, fx_values):
    """
    This function receives the universe and the values for x (`x_values`)
    and f(x) (`fx_values`).
    It generate new fx values for the given arguments, considering that it will fill the
    return np.array with zeroes for the f(x) of x that where not inside the range of `x_values`.
    It will also do a interpolation (using `np.interp`) for any value of of `x` that's defined
    in the universe and is inside of `x_values` range, but it's not present in x_values.
    """

    new_fx_values = fx_values
    missing_x_in_universe = False
    for x in universe:
        if x not in x_values:
            missing_x_in_universe = True
            break

    # this term don't have mf(x) values for all x values
    # present in the universe
    if missing_x_in_universe:
        # fill fx_values with 0 for the values that x can assume in the universe
        # and that are not present in the x_values, also
        # interpolate any values of fx that might be missing
        left_right_fills = 0.
        interp_fx_values = np.interp(
            universe,
            x_values,
            fx_values,
            left=left_right_fills,
            right=left_right_fills
        )
        new_fx_values = interp_fx_values
    return new_fx_values


class ScikitFuzzyFclListener(FclListener):
    """
    FclListener responsable for transforming the parsed Fcl file
    into corresponding scikit-fuzzy objects
    """
    def __init__(self):
        super(ScikitFuzzyFclListener, self).__init__()
        self.control_system = None
        self.vars = {}
        self.antecedents = {}
        self.num_steps = 100

    def visitErrorNode(self, node):
        raise FclParserException(node)

    def enterFunction_block(self, ctx):
        self.control_system = ControlSystem()

    def enterVar_def(self, ctx):
        var_id = ctx.ID().getText()
        var = {
            'type': ctx.data_type().getText(),
            'range': None
        }
        var_range = ctx.vrange()
        if var_range:
            var['range'] = [float(r.getText()) for r in var_range.REAL()]
        self.vars[var_id] = var

    def enterFuzzify_block(self, ctx):
        label = ctx.ID().getText()
        # if variable already defined a range then use this to instantiate the antecedent
        universe_range = self.vars.get(label, {}).get('range', None)
        self.antecedents[label] = {
            'value': Antecedent(universe_range, label=label),
            'terms': OrderedDict(),
        }

    def getLinguistic_term_var_dict(self, linguistic_term_ctx):
        var_dict = None
        if hasattr(linguistic_term_ctx.parentCtx, 'ID'):
            var_id = linguistic_term_ctx.parentCtx.ID().getText()
            var_dict = self.antecedents.get(var_id)
        else:
            var_id = linguistic_term_ctx.parentCtx.parentCtx.ID().getText()
            # var_dict = self.consequents.get(var_id)
        return var_dict

    def enterLinguistic_term(self, ctx):
        var_dict = self.getLinguistic_term_var_dict(ctx)
        term_id = ctx.ID().getText()
        var_dict.get('terms')[term_id] = {}

    def enterPiece_wise_linear(self, ctx):
        min_universe = 0
        max_universe = 0
        x_values = []
        fx_values = []
        for point in ctx.points():
            # TODO: Add support to ATOM as a ID in this point? or raise exception here?
            # won't support a ID as X, Y for now... considering that atom is only a REAL in this case
            x, y = [float(atom.getText()) for atom in point.atom()]
            x_values.append(x)
            fx_values.append(y)
            min_universe = min(x, min_universe)
            max_universe = max(x, max_universe)

        term_id = ctx.parentCtx.parentCtx.ID().getText()
        var_dict = self.getLinguistic_term_var_dict(ctx.parentCtx.parentCtx)
        # update this term information's dict
        var_dict.get('terms').update({
            term_id: {
                'x_values': x_values,
                'fx_values': fx_values,
                'min_universe': min_universe,
                'max_universe': max_universe,
                'mf_function': handle_piecewise_function,
                'mf_args_name': ['universe', 'x_values', 'fx_values']
            }
        })

    def enterSingleton(self, ctx):
        min_universe = 0
        max_universe = 0
        x_values = []
        fx_values = []

        x_value = float(ctx.atom().getText())
        fx_value = 1

        x_values.append(x_value)
        fx_values.append(fx_value)
        min_universe = x_value
        max_universe = x_value

        term_id = ctx.parentCtx.parentCtx.ID().getText()
        var_dict = self.getLinguistic_term_var_dict(ctx.parentCtx.parentCtx)
        # update this term information's dict
        var_dict.get('terms').update({
            term_id: {
                'x_values': x_values,
                'fx_values': fx_values,
                'min_universe': min_universe,
                'max_universe': max_universe,
                'mf_function': handle_piecewise_function,
                'mf_args_name': ['universe', 'x_values', 'fx_values']
            }
        })

    def update_universe_values(self, antecedent_label):
        antecedent_dict = self.antecedents.get(antecedent_label)
        universe = antecedent_dict.get('value').universe
        if len(universe.shape) != 0:
            min_universe, max_universe = universe[0], universe[-1]
        else:
            min_universe, max_universe = 0, 0

        x_values_set = set()
        # considering only piece_wise_linear terms for now
        for term_id, term_dict in antecedent_dict.get('terms').items():
            x_values_set.update(set(term_dict.get('x_values', [])))
            max_universe = max(max_universe, term_dict.get('max_universe', 0))
            min_universe = min(min_universe, term_dict.get('min_universe', 0))

        x_values_sorted = sorted(x_values_set)
        universe_dimension = len(x_values_sorted)
        if universe_dimension != 0:
            universe = np.asarray(x_values_sorted)
            antecedent_dict.get('value').universe = universe

    def exitFuzzify_block(self, ctx):
        label = ctx.ID().getText()
        self.update_universe_values(label)
        antecedent_dict = self.antecedents.get(label)
        universe = antecedent_dict.get('value').universe

        for term_id, term_dict in antecedent_dict.get('terms').items():
            mf_args_name = term_dict.get('mf_args_name', [])

            # prepare args for mf_function
            term_dict.update({'universe': universe})
            mf_args = [term_dict[k] for k in mf_args_name]

            mf_function = term_dict.get('mf_function')

            new_fx_values = mf_function(*mf_args)
            fx_values = new_fx_values

            # sets the x_values to used as the mf for this term in the skfuzz object
            antecedent_dict.get('value')[term_id] = fx_values
