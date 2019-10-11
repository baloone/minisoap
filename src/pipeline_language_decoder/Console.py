#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 18:30:22 2019

@author: chris
"""

from Preconditions import *

class Console():
    
    
    def __init__(self):
        self.decoder = None
        self.started = False
        self.thread = None
        
        
    def add_decoder(self, decoder):
        self.decoder = decoder
    
    def start(self):
        self.started = True
        self.thread = Thread(target=self.command)
        
        
    def command(self): 
        check(decoder, is not None)
        while(self.started):
            instruction = input("Write instruction\n")
            self.decoder.decode(instruction)
            
            
        
    def end(self):
        self.started = False