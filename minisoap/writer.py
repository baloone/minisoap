# Copyright (C) 2020 Nizar, Mohamed H
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

from .listener import Listener
from .stream import Stream
import subprocess as sp
from pathlib import Path
import tempfile, time

## Stream writer
#
# Writes a stream on hard drive
class Writer(Listener): 
    def __init__(self, stream, filename, chunk = None, samplerate = None, channels=None):
        if not isinstance(stream, Stream): raise TypeError
        Listener.__init__(self)
        self.path = Path(filename).absolute()
        self.stream = stream
        
    ## @var path
    # Path for the file
    
    ## @var stream
    # Stream to write
    
    ## @var chunk
    # Chunk size
    
    ## @var samplerate
    # Sampling rate
    
    ## @var Channels
    # Number of channels
    

    ## Run function of the thread, writes the stream to path
    #
    def run(self):
        command = [ "ffmpeg",
                "-f", 
                "f32le", 
                "-acodec", 
                "pcm_f32le",
                "-ac", str(self.stream.channels), 
                "-ar", str(self.stream.samplerate),
                '-i', '-', # The imput comes from a pipe
                '-y', # (optional) overwrite output file if it exists,
                self.path ]
        pipe = sp.Popen( command, stdin=sp.PIPE, stderr=sp.PIPE, stdout=sp.PIPE)
        _pcmbuf = pipe.stdin
        for data in self.stream:
            time.sleep(0.01)
            if self.killed():break
            _pcmbuf.write(data.tobytes())
            _pcmbuf.flush()
