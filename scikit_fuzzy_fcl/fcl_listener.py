# -*- coding: utf-8 -*-
from __future__ import absolute_import, division
from collections import OrderedDict
import sys

import numpy as np
from skfuzzy.control.controlsystem import ControlSystem
from skfuzzy.control.antecedent_consequent import Antecedent
from skfuzzy.membership import gaussmf

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
    universe_dimension = len(universe)
    # this term don't have mf(x) values for all x values
    # present in the universe
    if len(x_values) != universe_dimension:
        x_indexes_in_universe = [i for i, x in enumerate(universe) if x in x_values]
        init_x = x_indexes_in_universe[0]
        end_x = x_indexes_in_universe[-1]

        # fill y_values with 0 for the values that x can assume in the universe
        # and that are not present in the x_values
        zeros_fill_init = [0 for i in range(init_x)]
        zeros_fill_end = [0 for i in range((universe_dimension - 1) - end_x)]

        # interpolate any values of x that might be missing
        interp_y_values = np.interp(universe[init_x:end_x + 1], x_values, fx_values)
        new_fx_values = np.append(np.append(zeros_fill_init, interp_y_values), zeros_fill_end)
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
        # this is a orderect dict of the antecedents/consequents id's
        # self.terms = OrderedDict()

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

    def enterGauss(self, ctx):
        min_universe = 0
        max_universe = 0
        x_values = []
        y_values = []

        gauss_args = [float(atom.getText()) for atom in ctx.atom()]
        g_mean = gauss_args[0]
        g_sigma = gauss_args[1]

        # estimate universe
        min_universe = g_mean - (4.0 * g_sigma)
        max_universe = g_mean + (4.0 * g_sigma)

        x_values = np.linspace(min_universe, max_universe, num=self.num_steps)

        term_id = ctx.parentCtx.parentCtx.ID().getText()
        var_dict = self.getLinguistic_term_var_dict(ctx.parentCtx.parentCtx)
        # update this term information's dict
        var_dict.get('terms').update({
            term_id: {
                'x_values': x_values,
                'mean': g_mean,
                'sigma': g_sigma,
                'min_universe': min_universe,
                'max_universe': max_universe,
                'mf_function': gaussmf,
                'mf_args_name': ['universe', 'mean', 'sigma']
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
            # step_size = (max_universe - min_universe) / universe_dimension
            # new_universe = np.arange(min_universe, max_universe, step_size)
            universe = np.asarray(x_values_sorted)
            antecedent_dict.get('value').universe = universe

    def exitFuzzify_block(self, ctx):
        label = ctx.ID().getText()
        self.update_universe_values(label)
        antecedent_dict = self.antecedents.get(label)
        universe = antecedent_dict.get('value').universe

        for term_id, term_dict in antecedent_dict.get('terms').items():
            # x_values = term_dict.get('x_values')
            # y_values = term_dict.get('y_values')

            mf_args_name = term_dict.get('mf_args_name', [])

            # prepare args for mf_function
            term_dict.update({'universe': universe})
            mf_args = [term_dict[k] for k in mf_args_name]

            mf_function = term_dict.get('mf_function')

            new_y_values = mf_function(*mf_args)
            y_values = new_y_values

            # sets the x_values to used as the mf for this term in the skfuzz object
            antecedent_dict.get('value')[term_id] = y_values
