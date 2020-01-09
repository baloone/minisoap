#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 14:16:46 2020

@author: nizar
"""

from song import Song 
from writer import Writer

s = Song("../songs/jingles/Phased.wav")
w = Writer (s, "../songs/jingles/PhasedTest.wav")

w.run()