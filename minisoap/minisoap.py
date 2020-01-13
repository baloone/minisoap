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
DEBUG = False
VERSION = '0.1b'

import sys, os, signal, threading, traceback
from .parser import Parser, LineParsingError, ContinueParsing
from .console import Console
from .interpreter import InterpreterError, Interpreter
from .listener import Listener
from pathlib import Path
if os.name != "nt":
    import termios, tty

logo ="""                                                                                                                                
╔╦╗ ╦ ╔╗╔ ╦ ╔═╗ ╔═╗ ╔═╗ ╔═╗
║║║ ║ ║║║ ║ ╚═╗ ║ ║ ╠═╣ ╠═╝  """+VERSION+'  '+('debugging' if DEBUG else '')+"""
╩ ╩ ╩ ╝╚╝ ╩ ╚═╝ ╚═╝ ╩ ╩ ╩  
"""


def main(lines):
    console = Console()
    interpreter = Interpreter()
    parser = Parser()
    lines.reverse()
    cp = None
    console.log(logo, "\n> ", end="")
    bg = lambda cp: "> " if cp == None else ".. "
    while True:
        b = len(lines) > 0
        c = lines.pop() if b else console.input()
        if c != None:
            if b : console.log(bg(cp)+c+'\n', end="")
            try:
                try:
                    res = interpreter.run(parser.parse_line(c,cp))
                    cp = None
                    if res != None:
                        console.info(res) 
                except ContinueParsing as e:
                    cp = e
                except Exception as e:
                    console.error(e.__class__.__name__, e, join="\n")
                    if DEBUG:
                        console.error(traceback.format_exc())
                    cp = None
            except LineParsingError as e:
                console.error(e)

            if not b or (b and len(lines) == 0) : console.log(bg(cp), end="")
st = None
def ctrlc(sig, frame, st = None):
    print ('\nExiting...')
    [thread.kill() for thread in threading.enumerate()[1:] if isinstance(thread, Listener)]
    if st != None:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, st)
    sys.exit(1)

def wrapper():
    lines = []
    if len(sys.argv) > 1:
        p = Path(sys.argv[1])
        if p.exists():
            with open(p, 'r') as f:
                for line in f.readlines():
                    lines.append(line.replace('\n', ''))
                f.close()
    if os.name != "nt":
        st = termios.tcgetattr(sys.stdin)
        tty.setcbreak(sys.stdin.fileno())
        signal.signal(signal.SIGINT, lambda sig, frame:ctrlc(sig, frame, st))

        main(lines)
            
    else:
        signal.signal(signal.SIGINT, ctrlc)

        try:
            main(lines)
        except KeyboardInterrupt:
            pass

