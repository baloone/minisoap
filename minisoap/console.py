from colorama import init, Cursor, Fore, Back, Style
import os, sys


def getch():
    if os.name == 'nt':
        import msvcrt
        return ord(msvcrt.getch()) 
    else:
        return ord(str.encode(sys.stdin.read(1)))

def kbhit():
    if os.name == 'nt':
        import msvcrt
        return msvcrt.kbhit()
    else:
        from select import select
        dr,dw,de = select([sys.stdin], [], [], 0)
        return dr != []


class Console:
    def __init__(self):
        init()
        self.cursor_pos = 0
        self.line = ''
        self.hist_up = []
        self.hist_down = []
    def log(self, *args, end='\n'):
        """
        Equivalent to sys.stdout.write
        """
        if len(args) > 0:
            sys.stdout.write(args[0].__str__())
            for arg in args[1:]:
                sys.stdout.write(' ')
                sys.stdout.write(arg.__str__())
            sys.stdout.write(end)
            sys.stdout.flush()

    def info(self, *args):
        """
        Prints infos
        """
        sys.stdout.write(Back.BLUE + Fore.WHITE + 'INFO:' + Back.RESET + Fore.RESET + ' ')
        self.log(*args)

    def warn(self, *args):
        """
        Prints warnings
        """
        sys.stdout.write(Back.YELLOW + Fore.BLACK + 'WARNING:' + Back.RESET + Fore.RESET + ' ')
        self.log(*args)

    def error(self, *args):
        """
        Prints errors
        """
        sys.stdout.write(Back.RED + Fore.WHITE + 'ERROR:' + Back.RESET + Fore.RESET + ' ')
        self.log(*args)
    
    def input(self):
        """
        Non blocking input listener
        """
        ret = ord(b'\r') if os.name == "nt" else 10
        backspace = ord(b'\x08') if os.name == "nt" else 127
        mod = ord(b'\xe0') if os.name == "nt" else 27
        puts = lambda x : self.log(x, end='')
        def backspace_f():
            puts(Cursor.BACK()+self.line[self.cursor_pos:]+' '+Cursor.BACK(len(self.line)-self.cursor_pos+1))
            self.line = self.line[:self.cursor_pos-1] + self.line[self.cursor_pos:]
            self.cursor_pos-=1
            if self.cursor_pos < 0: self.cursor_pos = 0
        if kbhit():
            c = getch()
            if c == ret : 
                self.hist_up.append(self.line)
                self.line = ''
                self.cursor_pos = 0
                puts('\n')
                return self.hist_up[-1]
            elif c == backspace:
                backspace_f()
            elif c == mod:
                if not os.name == 'nt': getch()
                c = getch()
                K = ord(b'K') if os.name == 'nt' else 68
                M = ord(b'M') if os.name == 'nt' else 67
                H = ord(b'H') if os.name == 'nt' else 65
                P = ord(b'P') if os.name == 'nt' else 66
                S = ord(b'S') if os.name == 'nt' else 51
                if c == K and self.cursor_pos > 0: # left arrow
                    self.cursor_pos-=1
                    puts(Cursor.BACK())

                elif c == M and self.cursor_pos < len(self.line): # right arrow
                    self.cursor_pos+=1
                    puts(Cursor.FORWARD())

                elif c == H and len(self.hist_up) > 0: # up arrow
                    puts(Cursor.BACK(self.cursor_pos) + ' '*len(self.line) + Cursor.BACK(len(self.line)))
                    self.hist_down.append(self.line)
                    self.line = self.hist_up.pop()
                    self.log(self.line, end='')
                    puts(Cursor.BACK(len(self.line)))
                    self.cursor_pos=0

                elif c == P and len(self.hist_down) > 0: # down arrow
                    puts(Cursor.BACK(self.cursor_pos) + ' '*len(self.line) + Cursor.BACK(len(self.line)))
                    self.hist_up.append(self.line)
                    self.line = self.hist_down.pop()
                    self.log(self.line, end='')
                    puts(Cursor.BACK(len(self.line)))
                    self.cursor_pos=0

                elif c == S and self.cursor_pos < len(self.line): #suppr
                    self.cursor_pos+=1
                    puts(Cursor.FORWARD())
                    backspace_f()
            else:
                c = chr(c)
                puts(c+self.line[self.cursor_pos:]+Cursor.BACK(len(self.line)-self.cursor_pos)+(Cursor.FORWARD() if os.name != "nt" else ''))
                self.line = self.line[:self.cursor_pos] + c + self.line[self.cursor_pos:]
                self.cursor_pos+=1

        
    
