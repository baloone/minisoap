#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 13:39:04 2020

@author: nizar
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 12:02:52 2020

@author: nizar
"""
from threading import Thread
from stream import Stream
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
        pipe = sp.Popen( command, stdin=sp.PIPE, stderr=sp.STDOUT)
        self._pcmbuf = pipe.stdin
        for data in self.stream:
            self._pcmbuf.flush()
            self._pcmbuf.write(data.tobytes())
            print(1)
            
            
    