from .song import Song

class Builtins:
    '''
    Write all builtins functions here
    '''
    def __init__(self):
        self.steps = [] # list of the functions that should be launched at every step
    def tst(self, *args):
        print('hey', *args)
    def open(self, filepath):
        return Song(filepath)
    def write(self):
        pass