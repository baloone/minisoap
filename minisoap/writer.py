# Copyright (C) 2020 Nizar
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

from threading import Thread
from .stream import Stream
import subprocess as sp
from pathlib import Path

class Writer(Thread): 
    def __init__(self, stream, filename, chunk = None, samplerate = None, channels=None):
        if not isinstance(stream, Stream): raise TypeError
        Thread.__init__(self)
        self.path = Path(filename).absolute()
        self.stream = stream
        self.chunk = chunk if chunk != None else 4096
        self.samplerate = samplerate if samplerate != None else 44100
        self.channels = channels if channels != None else 2
        self.stream = stream


    def run(self):    
        command = [ "ffmpeg",
                "-f", 
                "f32le", 
                "-acodec", 
                "pcm_f32le",
                "-ac", str(self.channels), 
                "-ar", str(self.samplerate),
                '-i', '-', # The imput comes from a pipe
                '-y', # (optional) overwrite output file if it exists,
                self.path ]
        pipe = sp.Popen( command, stdin=sp.PIPE, stderr=sp.PIPE, stdout=sp.PIPE)
        self._pcmbuf = pipe.stdin
        for data in self.stream:
            self._pcmbuf.flush()
            self._pcmbuf.write(data.tobytes())
            
            
    
