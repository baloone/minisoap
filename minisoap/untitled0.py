#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 21:54:02 2020

@author: nizar
"""

from microphone import Microphone as m
import soundcard as sc


test = m()
p = sc.default_speaker().player(samplerate=48000)
    
for data in test:
    p.play(data)
    
    
