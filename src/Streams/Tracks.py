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
        print(data[0:100])
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
        print(self.int_byte_converter(self.data)[44:60])
        return self.header + self.int_byte_converter(self.data)
    
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
        step = self.nchannels
        returned = np.zeros((self.size,self.nchannels))
        for i in range(self.size):
                for k in range(self.nchannels):
                    start = i*self.samplewidth+k
                    end = start+self.nchannels*self.samplewidth
                    returned [i, k] = int.from_bytes(data[start:end:step], byteorder='big', signed=False)
        return returned
    
    #TODO 
    def int_byte_converter (self, array): 
        returned = []
        if self.nchannels == 2:
            for i in range(self.size):
                first, second = np.array(int.to_bytes(int(round(array[i, 0])), self.samplewidth, 'big')), np.array(int.to_bytes(int(round(array[i, 1])), self.samplewidth, 'big'))
                returned = np.append(returned, np.column_stack((first, second)).flatten()) 
                if (i == 0): 
                    print(first, "\n", second)
        else: 
            for i in range(self.size): 
                 returned = np.append(np.array(int.to_bytes(int(round(array[i])), self.samplewidth, 'big')))
        
        return returned.tobytes()
    
    def get_data_slice (self, start_time_in_milliseconds, end_time_in_milliseconds):
        return self.data[self.framerate*start_time_in_milliseconds:self.framerate*end_time_in_milliseconds]
                          
                        
            
                    
                    

    
    
        