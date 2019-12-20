import sys
from minisoap import Console, parse_line, LineParsingError, InterpreterError, Interpreter

logo ="""                                                                                                                                
╔╦╗ ╦ ╔╗╔ ╦ ╔═╗ ╔═╗ ╔═╗ ╔═╗
║║║ ║ ║║║ ║ ╚═╗ ║ ║ ╠═╣ ╠═╝  0.1a
╩ ╩ ╩ ╝╚╝ ╩ ╚═╝ ╚═╝ ╩ ╩ ╩  
"""


if __name__ == "__main__":
    console = Console()
    interpreter = Interpreter()
    console.log(logo, "\n> ", end="")
    while True:
        c = console.input()
        if c != None:
            try:
                try:
                    res = interpreter.run(parse_line(c))
                    if res != None:
                        console.info(res) 
                except InterpreterError as e:
                    console.error(e)
            except LineParsingError as e:
                console.error(e)

            console.log("> ", end="")
