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
from .song import Song, extensions
from pathlib import Path
import numpy as np

class Playlist(Stream):
    def __init__(self, dir_path, chunk = None, samplerate = None, channels=None):
        super(Playlist, self).__init__(chunk, samplerate, channels)
        self.path = Path(dir_path).absolute()
        self.songs = []
        self.loop = True
        if not self.path.exists(): raise Exception("Directory not found")
        if not self.path.is_dir(): raise Exception("Not a directory")
    def shuffle(self):
        self.songs = np.random.shuffle(self.songs)
        if hasattr(self, '_index'):
            self._index = 0
            self._current = iter(Song(self.songs[self._index]))
            self._next = iter(Song(self.songs[(self._index+1)%len(self.songs)]))

    def __iter__(self):
        for i in self.path.iterdir():
            if i.suffix[1:] in extensions: self.songs.append(i)
        if self.songs == []: return self
        self._index = 0
        self._current = iter(Song(self.songs[self._index]))
        self._next = iter(Song(self.songs[(self._index+1)%len(self.songs)]))
        return self
    def __next__(self):
        if self.songs == []: raise StopIteration
        try:
            return next(self._current)
        except:
            self._index += 1
            if self._index >= len(self.songs):
                if self.loop: self._index = 0
                else: raise StopIteration
            self._current = iter(Song(self.songs[self._index]))
            self._next = iter(Song(self.songs[(self._index+1)%len(self.songs)]))
            return next(self._current)
