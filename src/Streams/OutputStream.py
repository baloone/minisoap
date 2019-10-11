#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 14:16:04 2019

@author: nizar
"""
import wave
import math as m
from src.Preconditions import Preconditions as p
from Stream import Stream as s

class OutputStream (s): 
    
    writting_mode = 'wb'
       
    def __init__ (self, destination, launch = True, stereo=True, mono=False, samplewidth=2, framerate= 44100, nframes=1024): 
        super().__init__(destination, False, launch)
        self.wave_signal.setparams((0, samplewidth, framerate, nframes, 'NONE', 'NONE'))
        p.check(stereo != mono, "can't be mono and stereo and the same time")
        if(stereo): 
            self.set_as_stereo()
        else: 
            self.set_as_mono()
    
    def open(self): 
        super().open(OutputStream.writting_mode)
    
    def close(self):
        super().close()
       
    
    def write (self, data):
        p.check(not(self.infinite), "cannot completly load an infinite stream")
        try: 
            return self.wave_signal.writeframesraw(data)
        except:
            p.eprint("Error occured while writting the frames to destination", self.destination)
            
    def set_as_stereo(self):
        p.check(not(self.launched), "cannot verify if stereo for unopened stream")
        self.wave_signal.setnchannels(2)
    
    def set_as_mono(self): 
        p.check(not(self.launched), "cannot verify if mono for unopened stream")
        self.wave_signal.setnchannels(1)
    
    def set_sample_width (self, n):
        p.check(not(self.launched), "cannot obtain sample width for unopened stream")
        self.wave_signal.setsampwidth(n)
    
    def set_frame_rate(self, n): 
        p.check(not(self.launched), "cannot obtain frame rate for unopened stream")
        self.wave_signal.setframerate(n)

    def set_size (self, n): 
        p.check(not(self.launched), "cannot return size of unopened stream")
        self.wave_signal.setnframes(n)