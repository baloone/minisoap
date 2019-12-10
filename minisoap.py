import sys
from minisoap import Console
from minisoap import parse_line, LineParsingError

logo ="""                                                                                                                                
╔╦╗ ╦ ╔╗╔ ╦ ╔═╗ ╔═╗ ╔═╗ ╔═╗
║║║ ║ ║║║ ║ ╚═╗ ║ ║ ╠═╣ ╠═╝  0.1a
╩ ╩ ╩ ╝╚╝ ╩ ╚═╝ ╚═╝ ╩ ╩ ╩  
"""


if __name__ == "__main__":
    console = Console()
    console.log(logo, "\n> ", end="")
    while True:
        c = console.input()
        if c != None:
            try:
                console.info(parse_line(c))
            except LineParsingError as e:
                console.error(e)

            console.log("> ", end="")
