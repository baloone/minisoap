#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 10:43:05 2019

@author: chris
"""

from pipeline_language_decoder.Decoder import Decoder
from processor.Processor import Processor
from pipeline_language_decoder.Console import Console
import sys, os

def main(instructions):
    processor = Processor()

    decoder = Decoder(processor)

    console = Console(decoder)

    for i in instructions:
        console.run_instruction(i)

    console.start()
    
    
if __name__ == "__main__":
    if len(sys.argv) > 1:
        project_directory = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        path = os.sep.join(os.sep.join(sys.argv[1].split('/')).split('\\'))
        path = path if len (path) > 1 and (path[0] == '/' or path[0] == '.' or path[1] == ':') else os.path.join(project_directory, path)
        with open(path, 'r') as f:
            main(f.read().split("\n"))

    else: main([])