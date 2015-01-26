#! /usr/bin/env python

import sys
import random

import file_util as fu

'''
Description: this script is used to randomly shuffle data and split the data into train, devlopment and test data
Author: Mengwen Liu (mengwenliu09@gmail.com)
Create Date: 1/25/2015
Version: 1
'''

def shuffle_data(line_list):    #shuffle the data for ten times
    for i in range(0,10):
        random.shuffle(line_list)

    return line_list

def split_data(line_list, train_per, dev_per, test_per):
    if float(train_per) + float(dev_per) + float(test_per) != 1.0:
        print 'Percentage error!'
        sys.exit()
    else:
        num = float(len(line_list))
        test_num = int(float(test_per) * num) 
        dev_num = int(float(dev_per) * num)
        train_num = int(num - test_num - dev_num)

        train_list = line_list[0:train_num]
        dev_list = line_list[train_num:train_num+dev_num]
        test_list = line_list[train_num+dev_num:]
    return train_list, dev_list, test_list

def main():
    line_list = fu.readFile(sys.argv[1])
    line_list = shuffle_data(line_list)
    train_list, dev_list, test_list = split_data(line_list, \
                       sys.argv[2], sys.argv[3], sys.argv[4])
    fu.writeFile(train_list, sys.argv[5] + '-train')
    fu.writeFile(dev_list, sys.argv[5] + '-dev')
    fu.writeFile(test_list, sys.argv[5] + '-test')

if __name__ == '__main__':
    main() 
