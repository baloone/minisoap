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


def sine_n(A, n, f, start = 0, nchannels = 2, samplewidth = 2, fs=44100):
    frame_slice = np.arange(start, n)/fs
    samples = frame_slice
    for i in range(1,nchannels): 
        samples = np.column_stack((samples,frame_slice))
    signal = A*np.sin(2*np.pi*f*samples)
    return Track(signal, n, nchannels, samplewidth, fs)
    

def sine_t(A, t, f, start = 0, nchannels = 2, samplewidth = 2, fs=44100):
    return sine_n(A, t*fs, f, start = start*fs, nchannels = nchannels, samplewidth = samplewidth, fs= fs)
    
    

def constant_n(n, value, start = 0, nchannels = 2, samplewidth=2, fs=44100):
    frame_slice = np.arange(start, n)/fs
    samples = frame_slice
    for i in range(1,nchannels): 
        samples = np.column_stack((samples,frame_slice))
    signal = 0*samples + value
    return Track(signal, n, nchannels, samplewidth, fs)

def constant_t(t, value, start = 0, nchannels = 2, samplewidth = 2, fs=44100):
    return constant_n(t*fs, value, start = start*fs, nchannels = nchannels, samplewidth = samplewidth, fs= fs)
    
    