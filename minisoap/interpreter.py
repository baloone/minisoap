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
        map(lambda f: f(), self.builtins.steps)
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

