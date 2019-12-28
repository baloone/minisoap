# Copyright (C) 2019 Mohamed H
# 
# This file is part of Minisoap.
# 
# Minisoap is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Minisoap is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with Minisoap.  If not, see <http://www.gnu.org/licenses/>.

from .parser import Sequence, Expr, String, Number, VariableName
from .builtins import Builtins
class InterpreterError(Exception):
    pass

class Interpreter:
    def __init__(self):
        self.builtins = Builtins()
        self.builtins_names = [f for f in dir(Builtins) if callable(getattr(Builtins, f)) and not f.startswith("__")]
        self.variables = {}
    def step(self):
        self.builtins.clock.step()
    def run(self, seq):
        if seq.type == 'assign':
            if seq.variable_name.val in self.builtins_names: raise InterpreterError('Variable name not allowed')
            if seq.variable_name.val in self.variables: raise InterpreterError('Variable already defined')
            self.variables[seq.variable_name.val] = self.run_expr(seq.expr)
            return 'Variable ' + seq.variable_name.val + ' defined'
        else:
            return 'Value : ' + self.run_expr(seq.expr).__str__()
    def run_expr(self, expr):
        if isinstance(expr, String) or isinstance(expr, Number):
            return expr.val
        elif isinstance(expr, VariableName):
            if not expr.val in self.variables: raise InterpreterError('Use of undefined variable')
            return self.variables[expr.val]
        elif isinstance(expr, Expr):
            if not isinstance(expr.val, VariableName): raise InterpreterError('Cannot call a non callable')
            if not expr.val.val in self.builtins_names: raise InterpreterError('Unknown callable')
            return getattr(Builtins, expr.val.val)(self.builtins, *map(self.run_expr, expr.args))
        else: raise InterpreterError('Unrecognized expression')

