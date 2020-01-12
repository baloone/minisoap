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
from .generators import Silence
from .transition import Transition
from .song import Song, extensions
from pathlib import Path
import numpy as np
from functools import reduce

def bar(p1, p2, t):
    return t*p1+(1-t)*p2

## Playlist class
#
# Reads and operates over Songs form a folder
class Playlist(Stream):
    
    def __init__(self, dir_path, transition=Transition()):
        super(Playlist, self).__init__()
        self.path = Path(dir_path).absolute()
        self.songs = []
        self.loop = False
        self._index = 0
        self._tr = transition
        self._current = None
        self._next = None
        self._ic = None
        self._in = None
        self._trstr = None
        
        if not self.path.exists(): raise Exception("Directory not found")
        if not self.path.is_dir(): raise Exception("Not a directory")
        for i in self.path.iterdir():
            if i.suffix[1:] in extensions: self.songs.append(i)

        self.duration = reduce(lambda x,y: x+y, [Song(i).duration for i in self.songs])
    ## @var path
    # Path to the playlist folder
    
    ## @var songs
    # List containing the songs
    
    ## @var loop
    # Boolean on whether to loop over the playlist when done reading it
    
    ## @var _current
    # Current Song
    
    ## @var _next
    # Next Song
    
    ## @var _index
    # Index of current Song

    def _charge(self):
        snd = None
        if self._index+1 < len(self.songs):
            snd = Song(self.songs[self._index+1])
        elif self.loop:
            snd = Song(self.songs[0])
        self._current = self._next if self._next != None else Song(self.songs[self._index])
        self._next = snd
        self._ic = self._in if self._in != None else iter(self._current)
        self._in = iter(self._next) if self._next != None else None
    ## Shuffles songs in the playlist
    #
    def shuffle(self):
        np.random.shuffle(self.songs)
        self.__iter__()
    ## Iterates over the playlist
    #
    def __iter__(self):
        if self.songs == []: return self
        self._index = 0
        self._charge()
        return self
    
    ## Get next song
    #
    def __next__(self):
        if self.songs == [] or self._ic == None: raise StopIteration
        try:
            t = self._current.duration - self._current._t
            if t <= 0:
                self._charge()
                return next(self._ic)
            if t <= self._tr.duration:
                dt = 1.0/self.samplerate
                n1 = next(self._ic)
                n1 = np.concatenate((n1, np.zeros((self.chunk-len(n1), self.channels))))
                n2 = next(self._in) if self._in != None else np.zeros((self.chunk, self.channels))
                n2 = np.concatenate((np.zeros((self.chunk-len(n2), self.channels)), n2))
                f = [np.vectorize(lambda i: bar(n1[i][j], n2[i][j], self._tr.amplitude(t+i*dt))) for j in range(self.channels)]
                return np.transpose(np.array([f[i](np.arange(self.chunk)) for i in range(self.channels)]))
            else: return next(self._ic)
        except StopIteration:
            self._charge()
            return self.__next__()



""""
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
        self._in = iter(self._s2)
        self._c1 = None
        self._c2 = None
        return self
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


"""

