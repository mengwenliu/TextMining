#! /usr/bin/env python

'''
Description:
Author:
Create Date:
Version:
Core Function:
'''

import sys

def generateFeatureSet(token_list):
    feature_set = {}
    for i in range(len(token_list)):
        for token in token_list[i]:
            if token not in feature_set.keys():
                feature_set.setdefault(token, [])
            feature_set[token].append(i)
    return feature_set

def filterFeatureSet(threshold, feature_set):
    '''
    remove features occur less than certain times in the entire collection
    '''
    feature_set_red = {}
    for k, v in feature_set.items():
        if len(v) > int(threshold) and len(k) > 3:
            feature_set_red.setdefault(k, v)
    print 'threshold: ', threshold
    print 'number of features: ', len(feature_set_red)
    return feature_set_red

def removeSingleOccurrenceFeature(feature_set):
    '''
    remove featues that occur in only one file
    '''
    feature_set_red = {}
    for k, v in feature_set.items():
        file_set = set(v)
        if len(file_set) != 1:
            feature_set_red.setdefault(k, v)
    return feature_set_red
 
def generateFeatureVector(feature_set, num):
    feature_vec_list = []
    for i in range(num+1):
        #initialize vector for sents
        feature_vec_list.append([])
        feature_vec_list[i] = ['0'] * len(feature_set)
    for i, (k, v) in enumerate(sorted(feature_set.items())):
        feature_vec_list[0][i] = k
        for index in v:
            feature_vec_list[int(index)+1][i] = 1
    
    return feature_vec_list

def writeFeature(featureSet, filePath):
    with open(filePath, 'w+') as outputFile:
        for i, (k, v) in enumerate(sorted(featureSet.items())):
            outputFile.write(str(i) + '\t' +  k + \
                    '\t' + str(len(v)) + '\t' + \
                    '%s' % ','.join(map(str, v)) + '\n')
    print 'Finished: ' + filePath

def writeFeatureVector(feature_vec_list, filePath):
    with open(filePath, 'w+') as outputFile:
        for i in range(len(feature_vec_list)):
            outputFile.write('%s' % ','.join(map(str, \
                    feature_vec_list[i])) + '\n')
    print 'Finished: ' + filePath

