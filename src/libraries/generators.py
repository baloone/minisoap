#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 14:28:53 2019

@author: chris
"""
import numpy as np
import sys
sys.path.append('../')
from Streams.Tracks import Track


def sine_time(A, t, f, nchannels = 2, samplewidth = 2, fs=44100):
    sample = np.arange(t*fs)/fs
    samples = np.column_stack((sample,sample))
    signal = np.sin(2*np.pi*f*samples)
    return Track(signal, t*fs)
    
def sine_nframes(f,A, ):
    sample = np.arange(nframes)
    samples = sample
    for i in range(1,nchannels): 
        np.column_stack((samples,sample))
    signal = np.sin(2*np.pi*f*samples)
    return Track(signal, nframes, nchannels, samplewidth, framerate)
    
    

def constant(t, value, fs=44100):
    samples = np.arange(t*fs)/fs
    signal = 0*samples + value
    return signal
    

def square(t, f, a=1, fs=44100):
    return a*np.sign(sine(t, f, fs))