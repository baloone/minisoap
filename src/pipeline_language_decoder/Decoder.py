#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 18:30:21 2019

@author: chris
"""

from pipeline_language_decoder.Console import Console
from pipeline_language_decoder.Processor import Processor
from Preconditions import *

class Decoder():
        
    language_op = {
            
        "stop" : self.stop_console,
        "op" : self.decode_op,        
            
    }
    
    language_action = {
            
        "convolute" : ,
        "generate" : ,
            
    }

    def __init__(self):
        self.console = None
        self.processor = None
        
    
    def init_console(self, console):
        check(console, isinstance(Console))
        self.console = console
    
    def init_processor(self, processor):
        check(processor, isinstance(Processor))
        self.processor = processor
        
        
    def decode(self, instruction):
        
        try:
            parsed = instruction.split()
            # Parse message
            op = parsed[0]
            
            
            # Get op function
            operations.language.get()
        
            # Add op to processor pipeline
            processor.add_instruction()
        
            return language.get(instruction)
        
        except Exception as e:
            print("Error in language command" + e)
            
            
    def decode_operation(self, parsed):
        
    
    
    def stop_console(self):
        self.console.end()
        
    
    
    
    