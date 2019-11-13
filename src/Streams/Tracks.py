#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 23:47:04 2019

@author: nizar
"""
import numpy as np
import sys
sys.path.append('../')
import Preconditions as p

class Track ():
    
    
    wav_header_size = 44
 
    
    def __init__ (self, data, nframes, nchannels, samplewidth=2, framerate= 44100):
        self.size = nframes
        self.nchannels = nchannels
        self.samplewidth = samplewidth
        self.framerate = framerate
        if(type(data) == bytes):
            p.check(nframes*samplewidth*nchannels == len(data))
            self.data = self.byte_float_converter(data)
        else: 
            p.check(data.shape == (nframes, nchannels))
            self.data = np.array(data)
            
        
    def get_nchannels(self):
        return self.nchannels
    
    def get_raw_data(self):
        return self.float_byte_converter(self.data)
    
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
    
    def byte_float_converter (self, data): #can't use struct.unpack because of the 24 bit format.
        step = self.nchannels
        size = self.size
        samp = self.samplewidth
        returned = np.zeros((size,step))
        for i in range(size):
            for k in range(step):
                start = i*samp*step+k*samp
                end = start+ samp
                returned [i, k] = int.from_bytes(data[start:end], "big")
        return returned/2**(samp-1) - 1
    
    def float_byte_converter (self, array): 
        samp = self.samplewidth
        interm = (array+1) * 2**(samp-1)
        returned = bytes()
        for i in range(self.size):
            for k in range(self.nchannels):
                returned += int.to_bytes(int(interm[i, k]), samp, 'big') 
        return returned
    
    def get_data_slice (self, start_time_in_milliseconds, end_time_in_milliseconds):
        return self.data[self.framerate*start_time_in_milliseconds:self.framerate*end_time_in_milliseconds]
                          
                        
            
                    
                    

    
    
        