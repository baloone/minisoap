import sys
from minisoap.console import Console
from minisoap.parser import parse_line, LineParsingError

if __name__ == "__main__":
    console = Console()
    console.log("""Minisoap 0.1a\n> """, end="")
    while True:
        c = console.input()
        if c != None:
            try:
                console.info(parse_line(c))
            except LineParsingError as e:
                console.error(e)

            console.log("> ", end="")
