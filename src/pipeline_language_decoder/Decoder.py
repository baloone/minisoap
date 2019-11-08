from lark import Lark, Transformer

class Decoder(Transformer):
    
    grammar = Lark(r"""
    
    instruction: op args
    
    args: "[" [string* ("," string)*] "]"
    op: OP
    string: ESCAPED_STRING
    
    OP: "stop" | "open" | "close" | "sine" | "identity" | "crossfade_exp" | "nullify" 
    
    
    %import common.ESCAPED_STRING
    %import common.WS
    %ignore WS
    
    
    """, start = "instruction")
    
    def __init__(self, p):
        self.p = p
    
        self.op_d = {
                "open" : self.p.openn,
                "close" : self.p.close,
                "sine" : self.p.sine,
                "identity" : self.p.identity,
                "crossfade_exp" : self.p.crossfade_exp,
                "nullify" : self.p.nullify,
                "stop": self.p.stop
        }
        
        self.current_op = None
        
    def instruction(self, x):
        return list(x)
    
    def op(self, x):
        (x,) = x
        self.current_op = self.op_d.get(str(x))
        return str(x)
    
    def args(self, x):
        self.current_op(tuple(x))
        return tuple(x)
    
    def string(self, s):
        (s,) = s
        return s[1:-1]










