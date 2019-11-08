#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 19:55:58 2019

@author: chris
"""
from pipeline_language_decoder.Decoder import Decoder
from pipeline_language_decoder.Processor import Processor
from pipeline_language_decoder.Console import Console


processor = Processor()

decoder = Decoder(processor)

console = Console(decoder)

console.start()

text = 'sine ["arg1" ,"arg2"]'

Decoder.grammar.parse(text)

decoder.transform(Decoder.grammar.parse(text))
