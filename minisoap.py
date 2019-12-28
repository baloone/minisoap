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
