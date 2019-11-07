#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 16:18:45 2019

@author: chris
"""

from scipy.io import wavfile
from src.libraries.generators import *
from src.libraries.operations import *

fs, data = wavfile.read('src/libraries/example.wav')
plt.plot(data)


## Test op
seq1 = sine(2, 2)
seq2 = square(2, 2, a=0.8)



plt.plot(seq1)
plt.plot(seq2)

plt.plot(fade_exp(seq2, 0.99996))
plt.plot(fade_exp(seq1, 0.99996))
 
plt.plot(crossfade_exp(seq1, seq2, 0.99996))
 