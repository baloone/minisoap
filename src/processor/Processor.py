#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 00:55:09 2019

@author: chris
"""

import sys

class Processor():
    
    def __init__(self):
        return
    
    def openn(self, *args):
        print("OPEN")
        
    def close(self, *args):
        print("CLOSE")
    
    def sine(self, *args):
        print("SINE" + str(*args))
    
    def identity(self, *args):
        print("IDENTITY")
    
    def crossfade_exp(self, *args):
        print("CROSSFADE")
    
    def nullify(self, *args):
        print("NULLIFY" + str(*args))

    def stop(self, *args):
        exit(0)