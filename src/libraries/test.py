#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 16:18:45 2019

@author: chris
"""

from scipy.io import wavfile
from libraries.generators import *
from libraries.operations import *

## READ FILE
fs, data = wavfile.read('libraries/example.wav')
plt.plot(data)

## GENERATE WAVES
seq1 = sine(2, 2)
seq2 = square(2, 2, a=0.8)

plt.plot(seq1)
plt.plot(seq2)

plt.plot(fade_exp(seq2, 0.00001))
plt.plot(fade_exp(seq1, 0.00001))
 
plt.plot(crossfade_exp(seq1, seq2, 0.00001))
