#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 14:08:04 2019

@author: nizar
"""
import sys
import sounddevice as sd #low level library for soundcard(hardware) use
sys.path.append('../../')
import Preconditions as p
import Streams as s
from Tracks import Track 

class InputStream_SoundCard (s):
    
    def __init__ (self, nchannels, framerate, dtype=sd.default.dtype, device= sd.default.device, infinite= True, launch = True):
        self.framerate = framerate
        self.nchannels = nchannels
        self.samplewidth = 0
        self.stream = sd.InputStream(samplerate=framerate, device = device, channels=nchannels, dtype=dtype)
        super().__init__(device, infinite, launch)
        
        
    def open (self):
        self.stream.start()
        self.samplewidth = self.stream.samplesize
        
    def close (self): 
        self.stream.stop()
        
    def read(self, n):
        return Track(self.stream.read(n)[0], n, self.nchannels, self.samplewidth, self.framerate)
    
    def read_available(self, n):
        return Track(self.stream.read_available(n)[0], n, self.nchannels, self.samplewidth, self.framerate)
        
        
            
        
        
        