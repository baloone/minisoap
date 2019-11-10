#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 00:49:13 2019

@author: nizar
"""
from Tracks import Track
import math as m
import sys
sys.path.append('../')
import Preconditions as p
from Stream import Stream as s


class InputStream(s): 
    reading_mode = 'rb'
    def __init__ (self, source, infinite = False, launch = True): 
        super().__init__(source, infinite, launch)
    
    #wave parameters: (nchannels, sampwidth, framerate, nframes, 'NONE', 'not compressed')
    def open(self): 
        super().open(InputStream.reading_mode)
        self.wave_parameters = self.wave_signal.getparams()
        
    def close(self):
        super().close()
        
        
    def read_n_frames (self, n):
        p.check(self.launched, details ="cannot read unopened stream")
        p.check_in_range(n, endExclusive = self.size()+1)
        #try:
        x = self.wave_signal.readframes(n)
        #print(x)
        a = Track(x, n, stereo = self.stereo(), samplewidth = self.sample_width(), framerate = self.frame_rate()) 
        return a
        #except:
           # p.eprint("Error occured while reading the frames from source", self.file)
            
            
    def read_all (self):
        p.check(not(self.infinite), details ="cannot completly load an infinite stream")
        return self.read_n_frames(self.size())
    
    
    def stereo(self):
        p.check(self.launched, details ="cannot verify if stereo for unopened stream")
        return self.wave_parameters[0] - 1
    
    def mono(self): 
        p.check(self.launched, details ="cannot verify if mono for unopened stream")
        return self.wave_parameters[0] % 2
    
    def sample_width (self):
        p.check(self.launched, details ="cannot obtain sample width for unopened stream")
        return self.wave_parameters[1]
    
    def frame_rate(self): 
        p.check(self.launched, details ="cannot obtain frame rate for unopened stream")
        return self.wave_parameters[2]

    def size (self): 
        p.check(self.launched, details ="cannot return size of unopened stream")
        if (self.infinite):
            return m.inf
        else:
            return self.wave_parameters[3]
        
    def current_pos(self):
        p.check(self.launched, details ="cannot return pointer of unopened stream")
        return self.wave_signal.tell()
    
    def set_reading_pos (self, pos): 
        p.check(self.launched, details ="cannot modify pointer of unopened stream")
        p.check_in_range(pos, endExclusive=self.size())
        self.wave_signal.set(pos)
    
    
    
            