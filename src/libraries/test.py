#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 16:18:45 2019

@author: chris
"""

from scipy.io import wavfile
import matplotlib.pyplot as plt
import sys
sys.path.append('../')
from Streams.InputStream import InputStream as Input
import generators as g

#import operations as op

## READ FILE
T = Input("example.wav").read_all()
plt.plot(T.get_data())
plt.show()

## GENERATE WAVES
seq1 = g.sine_t(1, 2, 2).get_data()
seq2 = g.constant_t(2, 2).get_data()

plt.plot(seq1)
plt.show()
plt.plot(seq2)
plt.show()


#plt.plot(op.fade_exp(seq2, 0.00001))
#plt.plot(op.fade_exp(seq1, 0.00001))
 
#plt.plot(op.crossfade_exp(seq1, seq2, 0.00001))
