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
    int_size = 4
    
    def byte_int_converter (data):
        x = len(data)
        returned = np.zeros(x//4 + 1)
        i = 0
        for n in range(0,x,4):
            if(n <= x - 5):
                returned[i] = int.from_bytes(data[n:n+3], byteorder='big')
            else: 
                returned[i] = int.from_bytes(data[n:x-1-n], byteorder='big')
            i = i+1    
        return returned
    
    def __init__ (self, data, nframes, stereo=True, samplewidth=2, framerate= 44100):
        self.size = nframes
        self.raw_data = data
        print("here")
        unpacked = self.byte_int_converter(data)
        self.header = np.array(unpacked[0, 44])
        self.data = np.array(unpacked[44:])
        if (stereo):
            self.nchannels = 2
        else:
            self.nchannels = 1
        self.samplewidth = samplewidth
        self.framerate = framerate
        
    def get_nchannels(self):
        return self.nchannels
    
    def get_raw_data(self):
        #TODO
        return self.raw_data
    
    def get_data(self):
        return self.data
    
    def get_header(self):
        return self.header
    
    def get_size(self):
        return self.size 
    
    def get_samplewidth(self):
        return self.samplewidth
    
    def get_framerate(self):
        return self.framerate 
    
    
    
        