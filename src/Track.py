#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 15:27:40 2019

@author: chris
"""

from Preconditions import *

class Track:
    
    def __init__(self, sequence = bytes([])):
        check(sequence, lambda x: isinstance(x, bytes))
        self.sequence = sequence
        
        
    def get(self):
        return self.sequence