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

from .stream import Stream
import numpy as np

class Generator(Stream):
    def __init__(self, duration=float('inf'), chunk = None, samplerate = None, channels=None):
        if duration == None: duration = float('inf')
        self.duration = duration
        Stream.__init__(self, chunk, samplerate, channels)
    def _gen(self, size):
        return np.zeros((self.chunk, self.channels))
    def __iter__(self):
        self._t = 0.0
        return self
    def __next__(self):
        if self.duration < float('inf'):
            if self._t > self.duration: raise StopIteration
            a = int(self.duration-self._t)*self.samplerate
            if a < self.chunk:
                self.update_t(a)
                return self._gen(a)
        self.update_t()
        return self._gen(self.chunk)

class Silence(Generator):
    pass

class Sine(Generator):
    def __init__(self, freq=440, amplitude=1, duration=None, chunk = None, samplerate = None, channels=None):
        self._freq = freq
        self._amplitude = amplitude
        Generator.__init__(self, duration, chunk, samplerate, channels)
    def _gen(self, size):
        dt = float(self.chunk)/self.samplerate
        t = np.array([[self._t+i*dt]*self.channels for i in range(size)])
        return np.sin(2*np.pi*t*self._freq) * self._amplitude
        
