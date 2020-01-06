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
from pathlib import Path

logo ="""                                                                                                                                
╔╦╗ ╦ ╔╗╔ ╦ ╔═╗ ╔═╗ ╔═╗ ╔═╗
║║║ ║ ║║║ ║ ╚═╗ ║ ║ ╠═╣ ╠═╝  0.1a
╩ ╩ ╩ ╝╚╝ ╩ ╚═╝ ╚═╝ ╩ ╩ ╩  
"""


def main(lines):
    console = Console()
    interpreter = Interpreter()
    lines.reverse()

    console.log(logo, "\n> ", end="")
    while True:
        b = len(lines) > 0
        c = lines.pop() if b else console.input()
        if c != None:
            if b : console.log("> "+c+'\n', end="")
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

            if not b : console.log("> ", end="")
        interpreter.step()


if __name__ == "__main__":
    lines = []
    if len(sys.argv) > 1:
        p = Path(sys.argv[1])
        if p.exists():
            with open(p, 'r') as f:
                for line in f.readlines():
                    lines.append(line.replace('\n', ''))
                f.close()
    if os.name != "nt":
        import termios, tty
        st = termios.tcgetattr(sys.stdin)
        try:
            tty.setcbreak(sys.stdin.fileno())
            main(lines)
        except KeyboardInterrupt:
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, st)
    else: 
        try:
            main(lines)
        except KeyboardInterrupt:
            pass
