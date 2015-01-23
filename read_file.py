#! /usr/bin/env python

def readFile(file_path):
    line_list = []
    with open(file_path, 'r') as input_file:
        for line in input_file:
            line = line.strip()
            line_list.append(line)
    return line_list
