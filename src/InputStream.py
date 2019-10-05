#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 00:49:13 2019

@author: nizar
"""
import wave
import Preconditions as p
import Stream


class InputStream(Stream): 
    reading_mode = 'rb'
    def __init__ (self, source, infinite = False, launch = True): 
        super().__init__(source, infinite, launch)
        
    def open(self): 
        super().open(self.reading_mode)
        self.wave_parameters = self.wave_signal.getparams()
        
    def close(self):
        super().close()
        
        
    def read_n_frames (self, n):
        p.check(not(self.launched), "cannot read unopened stream")
        try:
            return self.wave_signal.readframes(n)
            
        except:
            p.eprint("Error occured while reading the frames from source", self.file)