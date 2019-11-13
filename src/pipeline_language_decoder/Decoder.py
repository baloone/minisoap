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
    
    instruction: op args | control_op
    
    control_op: CONTROL
    
    op: OP
    args: "["string* ("," string)*"]"
    
    string: ESCAPED_STRING
    
    CONTROL: "stop" | "execute" | "reset"
    
    OP: "open" | "close" 
      | "sine" | "constant" | "silence"
      | "identity" | "nullify" | "fade"
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
                "constant" : self.p.constant,
                "silence" : self.p.silence,
                "identity" : self.p.identity,
                "fade" : self.p.fade,
                "crossfade" : self.p.crossfade,
                "nullify" : self.p.nullify,
                "stop": self.p.stop,
                "execute": self.p.execute,
                "reset": self.p.reset
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
    
    ## op decoder
    #
    # Calls the processor's corresponding method for operations
    def op(self, x):
        (x,) = x
        self.current_op = self.op_d.get(str(x))
        return str(x)
    
    ## control_op decoder
    #
    # Calls the processor's corresponding method for control operations
    def control_op(self, x):
        (x,) = x
        self.op_d.get(str(x))()
        
    ## args rule decoder
    #
    # Save the arguments of the instruction
    def args(self, x):
        self.p.add(self.current_op, tuple(x))
        return tuple(x)
    
    ## string TERMINAL decoder
    def string(self, s):
        (s,) = s
        return s[1:-1]
    




