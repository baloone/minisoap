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
from pathlib import Path
import os, numpy, subprocess

class Song(Stream):
    def __init__(self, filename, chunk = 4096, samplerate = 44100, channels=2):
        Stream.__init__(self, chunk, samplerate, channels)
        exts = ["wav", "mp3", "flac", "aac", "m4a", "ogg"]
        if not filename.split('.')[-1] in exts : raise Exception("Extension not supported")
        self.path = Path(filename).absolute()
        if not os.path.exists(self.path): raise Exception("File not found")
        p = subprocess.Popen(["ffmpeg", "-i", filename, "-f", "f32le", "-acodec", "pcm_f32le",
                           "-ac", str(channels), "-ar", str(samplerate), "-"],
                          stdin=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self._pcmbuf = p.stdout

    def __str__(self):
        return 'Song('+self.path.__str__()+')'
    def __iter__(self):
        return self
    def __next__(self):
        a = self._pcmbuf.read(self.chunk*4*self.channels)
        if not len(a): raise StopIteration
        return numpy.frombuffer(a, dtype=numpy.float32).reshape((-1,2))
        


