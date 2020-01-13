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

## Generator class
#
# Generates synthetical waves
class Generator(Stream):
    
    def __init__(self, duration=float('inf')):
        Stream.__init__(self)
        self.duration = duration if duration != None else float('inf')

    
    ## @var duration
    # The duration of the wave
    
    
    ## Generates an empty wave
    #
    # @param The size of the wave
    def _gen(self, size):
        return np.zeros((size, self.channels))
    
    
    ## Iterate over the wave
    #
    def __iter__(self):
        self._t = 0.0
        return self
    
    ## Extract the next chunk
    #
    def __next__(self):
        
        if self.duration < float('inf'):
            if self._t > self.duration: raise StopIteration
            a = int((self.duration-self._t)*self.samplerate)
            if a == 0: raise StopIteration
            if a < self.chunk:
                self.update_t(a)
                return self._gen(a)
        self.update_t()
        return self._gen(self.chunk)

## Silent wave generator
#
# Generate a silent wave
class Silence(Generator):
    pass

## Sine wave generator
#
# Generate a sine wave
class Sine(Generator):
    def __init__(self, freq=440, amplitude=1, duration=None):
        self._freq = freq
        self._amplitude = amplitude
        self._i = 0
        Generator.__init__(self, duration)
    
    ## @var _freq
    # The frequency of the sine wave
    
    ## @var _amplitude
    # The amplitude of the sine wave
    
    ## Sine wave generator
    #
    # @param The size of the wave
    def _gen(self, size):
        dt = float(self.chunk)/self.samplerate
        t = np.array([[i*dt]*self.channels for i in range(self._i,self._i+size)])
        self._i+=size
        return np.sin(2*np.pi*t*self._freq) * self._amplitude
        





