#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 00:49:13 2019

@author: nizar
"""
import wave
import math as m
from src.Preconditions import Preconditions as p
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
        p.check(not(self.launched), "cannot read unopened stream")
        p.check_in_range(n, endExclusive = self.size()+1)
        try:
            return self.wave_signal.readframes(n)
            
        except:
            p.eprint("Error occured while reading the frames from source", self.file)
            
            
    def read_all (self):
        p.check(not(self.infinite), "cannot completly load an infinite stream")
        return self.read_n_frames(self.size())
    
    
    def stereo(self):
        p.check(not(self.launched), "cannot verify if stereo for unopened stream")
        return self.wave_parameters[0] - 1
    
    def mono(self): 
        p.check(not(self.launched), "cannot verify if mono for unopened stream")
        return self.wave_parameters[0] % 2
    
    def sample_width (self):
        p.check(not(self.launched), "cannot obtain sample width for unopened stream")
        return self.wave_parameters[1]
    
    def frame_rate(self): 
        p.check(not(self.launched), "cannot obtain frame rate for unopened stream")
        return self.wave_parameters[2]

    def size (self): 
        p.check(not(self.launched), "cannot return size of unopened stream")
        if (self.infinite):
            return m.inf
        else:
            return self.wave_parameters[3]
        
    def current_pos(self):
        p.check(not(self.launched), "cannot return pointer of unopened stream")
        return self.wave_signal.tell()
    
    def set_reading_pos (self, pos): 
        p.check(not(self.launched), "cannot modify pointer of unopened stream")
        p.check_in_range(pos, endExclusive=self.size())
        self.wave_signal.set(pos)
    
    
    
            