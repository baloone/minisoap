#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 14:28:53 2019

@author: chris
"""
import numpy as np
import matplotlib.pyplot as plt

def sine(t, f, fs=44100):
    samples = np.arange(t*fs)/fs
    signal = np.sin(2*np.pi*f*samples)
    return signal
    

def constant(t, value, fs=44100):
    samples = np.arange(t*fs)/fs
    signal = 0*samples + value
    return signal
    

def square(t, f, a=1, fs=44100):
    return a*np.sign(sine(t, f, fs))