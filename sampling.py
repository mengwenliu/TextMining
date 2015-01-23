#! /usr/bin/env python
# This script is used to select given number of samples from the input file
# author: Mengwen Liu (ml943@drexel.edu)
# date: 2/14/2014
# version: 1
# command: python sampling.py input_file number output_file


import sys
import random

fileList = []

with open(sys.argv[1], 'r') as inputFile:
    for line in inputFile:
        line = line.strip()
        if line:
            fileList.append(line)

sampleNum = int(sys.argv[2])

randomSample = random.sample(fileList, sampleNum)
output_file = open(sys.argv[3], 'w+')
output_file.write('%s' % '\n'.join(map(str, randomSample))) 
output_file.write('\n')
