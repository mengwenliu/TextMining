#! /usr/bin/env python

def readFile(file_path):
    line_list = []
    with open(file_path, 'r') as input_file:
        for line in input_file:
            line = line.strip()
            line_list.append(line)
    return line_list

def readFileToDict(file_path):
    line_dict = {}
    with open(file_path, 'r') as input_file:
        for i, line in enumerate(input_file):
            line = line.strip()
            if line:
                line_array = line.split('\t')
                line_dict.setdefault(line_array[0], i+1)
    return line_dict 


def writeFile(line_list, file_path):
    with open(file_path, 'w+') as output_file:
        output_str = '%s' % '\n'.join(map(str, line_list))
        output_file.write(output_str + '\n')
    print 'Finished: ', file_path
