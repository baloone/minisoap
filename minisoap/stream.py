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
# Represents a stream of samples as an Iterator
class Stream:
    def __init__(self, chunk = 4096, samplerate = 44100, channels=2):
        self.chunk = chunk if chunk != None else 4096
        self.samplerate = samplerate if samplerate != None else 44100
        self.channels = channels if channels != None else 2
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
    
    ## Go to next track
    #
    def __next__(self):
        raise StopIteration
    
    ## Update the number of seconds read from the stream
    #
    def update_t(self, chunk=None):
        c = self.chunk if chunk==None else chunk
        self._t += float(c)/self.samplerate
        
        
        
        
        
        
        