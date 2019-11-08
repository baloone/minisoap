#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 23:47:04 2019

@author: nizar
"""
import struct
import numpy as np

class Track ():
    
    header_size = 44
    
    def __init__ (self, data, stereo=True, samplewidth=2, framerate= 44100, nframes):
        self.size = nframes
        self.raw_data = struct.unpack("<%dh"%nframes, waveData)
        self.header = np.array(self.raw_data[0, header_size])
        self.data = np.array(self.raw_data[header_size:])
        if (stereo):
            self.nchannels = 2
        else:
            self.nchannels = 1
        self.samplewidth = samplewidth
        self.framerate = framerate
        
    def get_nchannels():
        return self.nchannels
    
    def get_raw_data ():
        return self.raw_data
    
    def get_data():
        return self.data
    
    def get_size():
        return self.size 
    
    def get_samplewidth():
        return self.samplewidth
    
    def get_framerate():
        return self.framerate 
    
        