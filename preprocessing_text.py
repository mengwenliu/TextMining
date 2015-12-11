#! /usr/bin/env python

'''
Description: preprocessing sentences, including converting 
             text to tokens, and a list of NLP techniques, i.e.
             tokenization, lemmatization, etc.
Author: Mengwen Liu (mengwenliu09@gmail.com)
Create Date: 1/23/2015
Version: 1
Core Function: text_to_token 
'''

import sys
import string

import nltk
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer


stop = stopwords.words('english')
sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
wnl = WordNetLemmatizer()

#convert a sentence to tokens 
#(applying tokenization, lemmatization, stopwords removal, etc.)
def text_to_token(sent):
    #tokens = pt.tokenization(sent)
    #lemma = tokenization(sent)
    lemma = lemmatization(sent)
    lower_lemma = to_lower_cases(lemma)
    filtered_lemma = remove_stopwords(lower_lemma)
    reduced_lemma = remove_non_alpha(filtered_lemma)
    return reduced_lemma

#(applying tokenization, lemmatization, uppercases to lowercases)
def text_to_token_simple(sent):
    lemma = lemmatization(sent)
    lower_lemma = to_lower_cases(lemma)
    return lower_lemma

#filtering
def remove_non_ascii(line):
    line = filter(lambda x: x in string.printable, line)
    return line

def filter_tokens(token_list):
    lower_tokens = to_lower_cases(token_list)
    non_stopword_tokens = remove_stopwords(lower_tokens)
    non_alpha_tokens = remove_non_alpha(non_stopword_tokens)
    
    return non_alpha_tokens
    
def remove_stopwords(token_list):
    new_token_list = [t for t in token_list if t not in stop]
    return new_token_list

def to_lower_cases(token_list):
    new_token_list = [t.lower() for t in token_list]
    return new_token_list

def remove_non_alpha(token_list):
    new_token_list = [t for t in token_list if t.isalpha()]
    return new_token_list

#sentence segmentation
def sentence_segmentation(line):
    sents = sent_tokenizer.tokenize(line)
    return sents

#tokenization
def tokenization(sent):
    tokens = nltk.word_tokenize(sent)
    return tokens

#tagging and lemmatizaion
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

def lemmatization(sent):
    tokens = tokenization(sent)
    tags = nltk.pos_tag(tokens)
    lemma = []
    for token, tag in tags:
        tag_category = penn_to_wn(tag)
        if tag_category != None:
            #lemm = wnl.lemmatize(token.lower(), tag_category)
            lemm = wnl.lemmatize(token, tag_category)
        else:
            #lemm = wnl.lemmatize(token.lower())    
            lemm = wnl.lemmatize(token)    
        lemma.append(lemm)
    #print sent
    #print lemma
    return lemma

# added on 12/9/2015
def remove_punctuation(token_list):
    new_token_list = [t for t in token_list if t not in string.punctuation]
    return new_token_list

