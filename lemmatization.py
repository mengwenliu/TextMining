#! /usr/bin/env python
# This script is used to do lemmatization using NLTK
# script name: lemmatization.py
# author: Mengwen Liu (mengwenliu09@gmail.com)
# vervion: 1
# create date: 1/2/2015

from nltk.corpus import wordnet as wn


def init():
    wnl = WordNetLemmatizer()
    stop = stopwords.words('english')
    stop.append('app')
    stop.append('apps')
    stop.append('u')

def is_noun(tag):
    return tag in ['NN', 'NNS', 'NNP', 'NNPS']

def is_verb(tag):
    return tag in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']

def is_adverb(tag):
    return tag in ['RB', 'RBR', 'RBS']

def is_adjective(tag):
    return tag in ['JJ', 'JJR', 'JJS']

def penn_to_wn(tag):
    if is_adjective(tag):
        return wn.ADJ
    elif is_noun(tag):
        return wn.NOUN
    elif is_adverb(tag):
        return wn.ADV
    elif is_verb(tag):
        return wn.VERB
    return None
