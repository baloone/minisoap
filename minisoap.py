import sys, os
from minisoap import Console, parse_line, LineParsingError, InterpreterError, Interpreter

logo ="""                                                                                                                                
╔╦╗ ╦ ╔╗╔ ╦ ╔═╗ ╔═╗ ╔═╗ ╔═╗
║║║ ║ ║║║ ║ ╚═╗ ║ ║ ╠═╣ ╠═╝  0.1a
╩ ╩ ╩ ╝╚╝ ╩ ╚═╝ ╚═╝ ╩ ╩ ╩  
"""


def main():
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
                except Exception as e:
                    console.error(e)
            except LineParsingError as e:
                console.error(e)

            console.log("> ", end="")
        interpreter.step()


if __name__ == "__main__":
    if os.name != "nt":
        import termios, tty
        st = termios.tcgetattr(sys.stdin)
        try:
            tty.setcbreak(sys.stdin.fileno())
            main()
        except KeyboardInterrupt:
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, st)
    else: 
        try:
            main()
        except KeyboardInterrupt:
            pass
