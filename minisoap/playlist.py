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
from .transition import TransitionStream, Transition
from .song import Song, extensions
from pathlib import Path
import numpy as np

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
        self._current = None
        self._next = None
        self._tr = transition
        self._trstr = None
        
        if not self.path.exists(): raise Exception("Directory not found")
        if not self.path.is_dir(): raise Exception("Not a directory")
    
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
    def _charge_trstr(self):
        snd = Silence(self._tr.duration)
        if self._index+1 < len(self.songs):
            snd = Song(self.songs[self._index+1])
        elif self.loop:
            snd = Song(self.songs[0])
        if self._trstr == None: self._trstr = TransitionStream(Song(self.songs[self._index]), snd, self._tr)
        else: self._trstr.add_stream(snd)
    ## Shuffles songs in the playlist
    #
    def shuffle(self):
        self.songs = np.random.shuffle(self.songs)
        if hasattr(self, '_index'):
            self._index = 0
            self._current = iter(Song(self.songs[self._index]))
            self._next = iter()

    ## Iterates over the playlist
    #
    def __iter__(self):
        for i in self.path.iterdir():
            if i.suffix[1:] in extensions: self.songs.append(i)
        if self.songs == []: return self
        self._index = 0
        self._charge_trstr()
        self._iter = iter(self._trstr)
        return self
    
    ## Get next song
    #
    def __next__(self):
        if self.songs == []: raise StopIteration
        if self._trstr._occured: self._charge_trstr()
        return next(self._iter)







