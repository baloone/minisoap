#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 00:55:09 2019

@author: chris
"""

import sys
from abc import ABCMeta, abstractmethod

# Implement all possible operations
# TODO niz replace args with the arguments that you need to run the function

class ProcessorArch(metaclass=ABCMeta):
    
    def __init__(self):
        self.stream_in = {}
        self.stream_out = {}
    
    ################# MAIN OPERATIONS
    @abstractmethod
    def openn(self, *args):
        pass
    
    @abstractmethod    
    def close(self, *args):
        pass
    
    @abstractmethod
    def stop(self, *args):
        exit(0)    
    
    ################# GENERATOR OPERATIONS
    @abstractmethod
    def sine(self, *args):
        pass
    
    ################# OPERATOR ON STREAMS
    @abstractmethod
    def identity(self, *args):
        pass
    
    @abstractmethod
    def crossfade(self, *args):
        pass
    
    @abstractmethod
    def nullify(self, *args):
        pass







