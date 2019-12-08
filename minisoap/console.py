from colorama import init, Cursor, Fore, Back, Style
import os



class Console:
    def __init__(self):
        init()
        self.cursor_pos = 0
        self.line = ''
        self.hist_up = []
        self.hist_down = []
    def log(self, *args, end='\n'):
        print(*args, end=end)

    def info(self, *args):
        print(Back.BLUE + Fore.WHITE + 'INFO:' + Back.RESET + Fore.RESET, end=' ')
        self.log(*args)

    def warn(self, *args):
        print(Back.YELLOW + Fore.BLACK + 'WARNING:' + Back.RESET + Fore.RESET, end=' ')
        self.log(*args)

    def error(self, *args):
        print(Back.RED + Fore.WHITE + 'ERROR:' + Back.RESET + Fore.RESET, end=' ')
        self.log(*args)
    
    def input(self):
        puts = lambda x : print(x, end='')
        if os.name=='nt':
            import msvcrt
            while True:
                if msvcrt.kbhit():
                    c = msvcrt.getch()
                    if c == b'\r' : 
                        self.hist_up.append(self.line)
                        self.line = ''
                        self.cursor_pos = 0
                        puts('\n')
                        return self.hist_up[-1]
                    elif c == b'\x08':
                        puts(Cursor.BACK() + ' ' + Cursor.BACK())
                    elif c == b'\xe0':
                        c = msvcrt.getch()

                        if c == b'K' and self.cursor_pos > 0: # left arrow
                            self.cursor_pos-=1
                            puts(Cursor.BACK())

                        if c == b'M' and self.cursor_pos < len(self.line)-1: # right arrow
                            self.cursor_pos+=1
                            puts(Cursor.FORWARD())

                        if c == b'H' and len(self.hist_up) > 0: # up arrow
                            puts(Cursor.BACK(self.cursor_pos) + ' '*len(self.line) + Cursor.BACK(len(self.line)))
                            self.hist_down.append(self.line)
                            self.line = self.hist_up.pop()
                            self.log(self.line, end='')
                            puts(Cursor.BACK(len(self.line)))
                            self.cursor_pos=0

                        if c == b'P' and len(self.hist_down) > 0: # down arrow
                            puts(Cursor.BACK(self.cursor_pos) + ' '*len(self.line) + Cursor.BACK(len(self.line)))
                            self.hist_up.append(self.line)
                            self.line = self.hist_down.pop()
                            self.log(self.line, end='')
                            puts(Cursor.BACK(len(self.line)))
                            self.cursor_pos=0

                        if c == b'S' and self.cursor_pos < len(self.line):
                            puts(self.line[self.cursor_pos+1:]+' '+Cursor.BACK(len(self.line)-self.cursor_pos))
                            self.line = self.line[:self.cursor_pos] + self.line[self.cursor_pos+1:]

                    else:
                        c = ''.join(map(chr, c))
                        puts(c+self.line[self.cursor_pos:]+Cursor.BACK(len(self.line)-self.cursor_pos))
                        self.line = self.line[:self.cursor_pos] + c + self.line[self.cursor_pos:]
                        self.cursor_pos+=1
        else:
            return input()

        
    
