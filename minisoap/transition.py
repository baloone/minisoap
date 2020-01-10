# Copyright (C) 2020 Mohamed H
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

from .stream import Stream
import numpy as np

def bar(p1, p2, t):
    return t*p1+(1-t)*p2

class Transition:
    def __init__(self, table=[]):
        self.duration = 0 if table == [] else max([i[0] for i in table])
        self._table = sorted(table)
    
    def amplitude(self, t):
        """
        Linear approximation of the transition table
        Returns amplitude of the stream which is ending
        t in s
        """
        try:
            i = len(self._table)-1
            while self._table[i][0] > t: i-=1
            t1,a1=self._table[i]
            t2,a2=self._table[i+1]
            return (a2-a1)/(t2-t1)*(t-t1)           
        except:
            return 0
    def __str__(self):
        return 'Transition(\n.     '+"\n.     ".join([str(t[0])+"s ->> "+str(t[1]) for t in self._table])+'\n)'


class TransitionStream(Stream):
    def __init__(self, stream1, stream2, transition=Transition()):
        super(TransitionStream, self).__init__()
        self._s1 = stream1
        self._s2 = stream2
        self._tr = transition
        self._occured = False
        self.duration = self._s1.duration + self._s2.duration - self._tr.duration
    def __iter__(self):
        self._is1 = iter(self._s1)
        self._is2 = iter(self._s2)
        self._c1 = None
        self._c2 = None
        return self
    def add_stream(self, stream):
        if not self._occured: raise Exception('Cannot add a stream')
        self._s1, self._s2 = self._s2, stream
        self._is1, self._is2 = self._is2, iter(self._s2)
        self._occured = False
        self.duration = self._s1.duration + self._s2.duration - self._tr.duration
    def __next__(self):
        t = self._s1.duration - self._s1._t
        if t <= 0:
            self._occured = True
            return next(self._is2)
        if t <= self._tr.duration:
            dt = 1.0/self.samplerate
            n1 = next(self._is1)
            n1 = np.concatenate((n1, np.zeros((self.chunk-len(n1), self.channels))))
            n2 = next(self._is2)
            n2 = np.concatenate((np.zeros((self.chunk-len(n2), self.channels)), n2))
            f = [np.vectorize(lambda i: bar(n1[i][j], n2[i][j], self._tr.amplitude(t+i*dt))) for j in range(self.channels)]
            return np.transpose(np.array([f[i](np.arange(self.chunk)) for i in range(self.channels)]))
        else: return next(self._is1)
