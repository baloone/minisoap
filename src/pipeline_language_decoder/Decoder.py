#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 18:30:21 2019

@author: chris
"""

from pipeline_language_decoder.Console import Console
from pipeline_language_decoder.Processor import Processor
from libraries.generators import *
from libraries.operations import *
from Preconditions import *


class Decoder():

    ## Example language
    ## op convolute **targets **args
    ## gen sine **args
      
    language_basic = {
            
        "stop" : self.stop_console,
        "op" : self.decode_operation,
        "gen": self.decode_generator
            
    }
    
    language_op = {
            
        "amplitude" : ,
        "convolute" : ,
        "fade_exp" : ,
        "fade_lin" : ,
        "convolute" : 
            
    }
    
    
    language_gen = {
            
        "sine" : sine,
        "square" : square,
        "constant" : constant
            
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
            # Parse message
            parsed = instruction.split()
            
            
            op = parsed[0]
            t = parsed[-1]
            
            
            # Get op function
            def run_instruction():
                return Decoder.language.get()(parsed)
        
            # Add op to processor pipeline
            processor.add_instruction((t, run_instruction))
            
        except Exception as e:
            print("Error in language command" + e)
            
            
    def decode_operation(self, parsed):
        
        op = parsed[1]
        args = parsed[1:-1]
        
        return language_op.get(op)(args)
        
        
    def decode_generator(self, parsed):
        op = parsed[1]
        args = parsed[1:-1]
        
        return language_gen.get(op)(args)
        
    
    def stop_console(self):
        self.console.end()
        
    
    
    
    