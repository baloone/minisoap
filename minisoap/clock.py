from datetime import datetime

class Clock:
    def __init__(self):
        self.exs = []
    def step(self):
        t = datetime.now()
        l = []
        while len(self.exs):
            d, f = self.exs.pop()
            if d <= t: f()
            else: l.append(d, f)
        self.exs = l
    def wait(self, d, f):
        self.exs.append((d, f))

