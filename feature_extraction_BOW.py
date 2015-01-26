#! /usr/bin/env python

'''
Description:
Author:
Create Date:
Version:
Core Function: featureExtraction
'''

import sys

def featureExtraction(all_token_list, threshold, boolean):
    feature_set = generateFeatureSet(all_token_list)
    feature_set_red = removeSingleOccurrenceFeature(feature_set)
    feature_set_final = filterFeatureSet(threshold, feature_set_red)
    if boolean:
        feature_vector_list = generateFeatureVector( \
                    feature_set_final, len(all_token_list), True)
    else:
        feature_vector_list = generateFeatureVector( \
                    feature_set_final, len(all_token_list), False)
    return feature_set_final, feature_vector_list


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
 
def generateFeatureVector(feature_set, num, boolean):
    feature_vec_list = []
    for i in range(num):
        #initialize vector for sents
        feature_vec_list.append([])
        feature_vec_list[i] = ['0'] * len(feature_set)
    if boolean:
        for i, (k, v) in enumerate(sorted(feature_set.items())):
            for index in v:
                feature_vec_list[int(index)][i] = 1
    else:
        for i, (k, v) in enumerate(sorted(feature_set.items())):
            indices = set(v)
            for index in indices:
                feature_vec_list[int(index)][i] = v.count(index)
    
    return feature_vec_list

def generateFeatureVectorForTest(feature_set, all_token_list, boolean):
    '''
    feature_set format: 
    key: word
    value: index (starting from 1)
    '''
    feature_vec_list = []
    for i in range(len(all_token_list)):
        vector = [0] * len(feature_set)
        for token in all_token_list[i]:
            if token in feature_set.keys():
                if boolean:
                    vector[feature_set[token]-1] = 1    
                else:
                    vector[feature_set[token]-1] += 1
        feature_vec_list.append(vector)
    return feature_vec_list

def writeFeature(featureSet, filePath):
    with open(filePath, 'w+') as outputFile:
        for i, (k, v) in enumerate(sorted(featureSet.items())):
            #feature index starting from 1
            outputFile.write(str(i+1) + '\t' +  k + \
                    '\t' + str(len(v)) + '\t' + \
                    '%s' % ','.join(map(str, v)) + '\n')
    print 'Finished: ' + filePath

def writeFeatureVector(feature_vec_list, filePath):
    with open(filePath, 'w+') as outputFile:
        for i in range(len(feature_vec_list)):
            outputFile.write('%s' % ','.join(map(str, \
                    feature_vec_list[i])) + '\n')
    print 'Finished: ' + filePath

def generateSparseFeatureVector(featureList):
    featureDict = {}
    for i in range(len(featureList)):
        featureDict.setdefault(i, [])
        for j in range(len(featureList[i])):
            if int(featureList[i][j]) != 0:
                featureDict[i].append((j+1, featureList[i][j]))
    return featureDict

def writeSparseFeatureVector(featureList, filePath):
    featureDict = generateSparseFeatureVector(featureList)
    with open(filePath, 'w+') as outputFile:
        for i in range(len(featureList)):
            featureIndex = [str(v1) + ':' + str(v2) for v1, v2 in sorted(featureDict[i])]
            outputFile.write('%s' % ' '.join(map(str, featureIndex)) + '\n')
    print 'Finished: ' + filePath
