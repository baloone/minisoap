#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 16:18:45 2019

@author: chris
"""

import matplotlib.pyplot as plt
import sys
sys.path.append('../')
from Streams.InputStream import InputStream as Input
from Streams.OutputStream import OutputStream as Output
import operations as op
import generators as g

#import operations as op

## READ FILE

K = Input("example.wav")
T = K.read_all()
plt.plot(T.get_data())
plt.show()
K.close()


## GENERATE WAVES
seq1 = g.sine_t(1, 2, 2).get_data()
seq2 = g.constant_t(2, 2).get_data()

plt.plot(seq1)
plt.show()
plt.plot(seq2)
plt.show()

O = op.add(T, op.nullify(T), 0)

plt.plot(O.get_data())
plt.show()
w = Output("example_faded.wav", O)
w.write()
w.close()

#plt.plot(op.fade_exp(seq1, 0.00001))
 
#plt.plot(op.crossfade_exp(seq1, seq2, 0.00001))
