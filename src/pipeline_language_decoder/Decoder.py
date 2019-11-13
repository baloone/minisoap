from lark import Lark, Transformer
from processor.Processor import Processor

## Decoder
#
# This object is the decoder of the Minisoap that will translate user's instructions into processor commands
class Decoder(Transformer):
    
    ## Grammar of decoder
    #
    # Grammar format from Lark library
    # Describes the language in a format called EBNF
    # rule_name : list of rules and TERMINALS to match
    # TERMINAL: string or a regular expression
    grammar = Lark(r"""
    
    instruction: op [args]
    
    args: "[" [string* ("," string)*] "]"
    op: OP
    string: ESCAPED_STRING
    
    OP: "stop" 
      | "open" | "close" 
      | "sine" | "constant" | "silence"
      | "fade"
      | "crossfade" 
    
    
    %import common.ESCAPED_STRING
    %import common.WS
    %ignore WS
    
    
    """, start = "instruction")
    
    
    ## Decoder constructor
    #
    #  @param self Object's pointer
    #  @param processor Minisoap's processor pointer
    def __init__(self, processor):
        self.p = processor
    
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
    
    ## @var p
    #  Minisoap's processor pointer
    
    ## @var op_d
    #  Dictionary containing decoder's dispacher for user's instructions
    
    ## @var current_op
    #  Tuple storing current instruction's args
    
    ## Instruction rule decoder
    def instruction(self, x):
        return list(x)
    
    ## op TERMINAL decoder
    #
    # Calls the processor's corresponding method
    def op(self, x):
        (x,) = x
        if(str(x) == "stop"):
            self.op_d.get(str(x))()
        else:    
            self.current_op = self.op_d.get(str(x))
        return str(x)
    
    ## args rule decoder
    #
    # Save the arguments of the instruction
    def args(self, x):
        self.current_op(tuple(x))
        return tuple(x)
    
    ## string TERMINAL decoder
    def string(self, s):
        (s,) = s
        return s[1:-1]
    




