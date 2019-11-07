#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 15:22:14 2019

@author: chris
"""

import numpy as np



def nullify(seq):
    return 0*seq


def amplitude(seq, a):
    return a*seq


def convolve(seq1, seq2):
    return np.convolve(seq1, seq2)


def add(seq1, seq2, a1=0.5, a2=0.5):
    return a1*seq1 + a2*seq2


def fade_exp(seq, factor):
    return np.array([seq[k]*factor**k for k in range(len(seq))])


def fade_lin(seq, speed):
    return np.array([(seq[k] - np.sign(seq[k])*speed*k) for k in range(len(seq))])


def crossfade_exp(seq1, seq2, factor):
    return fade_exp(seq1, factor) + np.flip(fade_exp(seq2, factor))


def crossfade_lin(seq1, seq2, speed):
    return fade_lin(seq1, speed) + np.flip(fade_lin(seq2, -speed))


