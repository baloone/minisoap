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


## Stream class
#
# Represents a stream
class Stream(object):
    def __init__(self):
        self.chunk = 4096
        self.samplerate = 44100
        self.channels = 2
        self.duration = float('inf')
        self._t = 0.0
        
    ## @var chunk
    # The number of chunks
    
    ## @var samplerate
    # The samplerate of the stream
    
    ## @var channels
    # The number of channels of the stream
    
    ## @var duration
    # The duration of the stream (inf)
    
    ## @var _t
    # The number of seconds read from the stream
    
    ## Iterate over the stream
    #
    def __iter__(self):
        return self
    
    ## Next function of the stream iterator
    #
    def __next__(self):
        raise StopIteration
    
    ## Update the number of seconds read from the stream
    #
    def update_t(self, chunk=None):
        c = self.chunk if chunk==None else chunk
        self._t += float(c)/self.samplerate

## Mix class
#
# Mix two streams
class Mix(Stream):
    def __init__(self, mainstream, bgstream, p=.5):
        super(Mix, self).__init__()
        self._s1 = mainstream if mainstream!=None else Stream()
        self._s2 = bgstream if bgstream!=None else Stream()
        self._p = p
        self.duration = max(self._s1.duration, self._s2.duration)
    
    ## @var _s2
    # Second stream
    
    ## @var _s1
    # First stream
    
    ## @var _p
    # Amplitude of first stream (second stream 1 - _p)
    
    
    ## Iterate over the stream
    #
    def __iter__(self):
        self._s1 = iter(self._s1)
        self._s2 = iter(self._s2)
        return self
    
    ## Next function of the stream iterator, mixes the two streams
    #
    def __next__(self):
        ret = None
        n1 = next(self._s1)
        try:
            n2 = next(self._s2)
            ret = self._p * n1 + (1-self._p) * n2
        except:
            ret = self._p * n1
        self.update_t()
        return ret
