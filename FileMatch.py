#!/usr/bin/env python
## This takes in two text files and calculate the similarity between them. We clean the text for comparison by 1) lowercasing the words, and 2) write out shorten words like "you'll" to "you will" so that they are uniformly presented among the sample texts. The similarity is calculated as the ratio of the number of overlapping words between two texts to the total number of unique words in the text. It will have a value of 1 if the unique words between the two texts are the same and 0 if there are no words in common.

import argparse
import re

def txt_to_str(file):
    with open(file, 'r') as f:
        data = f.read().replace('\n', '').lower()
        data = re.sub('don\'t', 'do not', data)
        data = re.sub('you\'ll', 'you will', data)
        data = re.sub('we\'ll', 'we will', data)
    return data

def get_similarity_ratio(str1, str2): 
    # create lists to use intersection for comparison
    set1 = set(str1.split()) 
    set2 = set(str2.split())
    intset = set1.intersection(set2)
	# return the number of common words divided by 
	# (the number of words in both strings less the number common words).
	# i.e. 5 in both files all 5 common 5/(5+5-5) = 1.0
	# i.e. 4 vs 5 words the files with 4 common 4/(4+5-4) = .8
    return float(len(intset)) / (len(set1) + len(set2) - len(intset))

def text_sim(text1, text2):
    str1 = txt_to_str(text1)
    str2 = txt_to_str(text2)
    return get_similarity_ratio(str1,str2)

parser = argparse.ArgumentParser()
parser.add_argument("text_file_1", help="the path of the first text file")
parser.add_argument("text_file_2", help="the path of the second text file")
args = parser.parse_args()

print 'The similiarity between', args.text_file_1, 'and', args.text_file_2, 'is', text_sim(args.text_file_1, args.text_file_2)
#print('The similiarity between', args.text_file_1, 'and', args.text_file_2, 'is', text_sim(args.text_file_1, args.text_file_2))
