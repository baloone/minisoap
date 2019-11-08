#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 23:47:04 2019

@author: nizar
"""
import struct
import numpy as np

class Track ():
    
    
    wav_header_size = 44
    
    
    def __init__ (self, data, nframes, stereo=True, samplewidth=2, framerate= 44100):
        self.size = nframes
        print("here")
        if (stereo):
            self.nchannels = 2
        else:
            self.nchannels = 1
        self.samplewidth = samplewidth
        self.framerate = framerate
        self.header = data[0:self.wav_header_size-1]
        self.data = self.byte_int_converter(data[self.wav_header_size:])
        
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
    
    def byte_int_converter (self, data):
        returned = np.zeros((self.size,self.nchannels))
        for i in range(self.size):
                for k in range(self.nchannels):
                    returned [i, k] = int.from_bytes(data[i*self.sampewidth+k:i+self.nchannels*self.samplewidth-1:self.nchannels], byteorder='big', signed=False)
        return returned
    
    def int_byte_converter (self, array): 
        returned = bytearray()
        for i in range(self.size):
                if self.nchannels == 2:
                    first, second = int.to_bytes(array[i, 0], self.samplewidth, 'big'), int.to_bytes(array[i, 1], self.samplewidth, 'big')
                    
                    

    
    
        