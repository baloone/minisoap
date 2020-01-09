#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 21:54:02 2020

@author: nizar
"""

from microphone import Microphone as m
import soundcard as sc
import numpy

# =============================================================================
# speakers = sc.all_speakers()
# # get the current default speaker on your system:
default_speaker = sc.default_speaker()
# # get a list of all microphones:
# mics = sc.all_microphones()
# # get the current default microphone on your system:
default_mic = sc.default_microphone()
# # record and play back one second of audio:
# data = default_mic.record(samplerate=48000, numframes=48000)
# default_speaker.play(data/numpy.max(data), samplerate=48000)
# =============================================================================
test = m()
print("l")
with default_speaker.player(samplerate=44100) as sp:
    while(True):
        data = test.__next__()
        sp.play(data)

# =============================================================================
# test = m()
# p = sc.default_speaker().player(samplerate=44100)
#     
# for data in test:
#     p.play(data)
# =============================================================================
    
    
