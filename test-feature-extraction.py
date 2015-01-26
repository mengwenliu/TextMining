#! /usr/bin/env python

import sys


sys.path.append('/Users/mengwen/Documents/workspace/python/my_python_modules')

import preprocessing_text as pt
import feature_extraction_BOW as feb
import file_util as fu


def main():
    feature_dict = fu.readFileToDict(sys.argv[1])
    test_data = fu.readFile(sys.argv[2]) 
    all_normalized_tokens = []
    for line in test_data:
        line = pt.remove_non_ascii(line)
        sents = pt.sentence_segmentation(line)
        normalized_tokens = [] 
        for sent in sents:
            tokens = pt.text_to_token(sent)
            normalized_tokens.extend(tokens)
        all_normalized_tokens.append(normalized_tokens)
    print all_normalized_tokens
    feature_vector_list = feb.generateFeatureVectorForTest(feature_dict, all_normalized_tokens, False)
    print feature_vector_list

if __name__ == '__main__':
    main()
