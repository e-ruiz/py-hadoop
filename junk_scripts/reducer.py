#!/usr/bin/env python3
"""A more advanced Reducer, using Python iterators and generators."""

from itertools import groupby
from operator import itemgetter
import sys

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 


def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.lower().rstrip().split(separator, 1)

def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_mapper_output(sys.stdin, separator=separator)
    # groupby groups multiple word-count pairs by word,
    # and creates an iterator that returns consecutive keys and their group:
    #   current_word - string containing a word (the key)
    #   group - iterator yielding all ["&lt;current_word&gt;", "&lt;count&gt;"] items
    for current_word, group in groupby(data, itemgetter(0)):
        # ignoring english stopwords
        # it is very faster than map without stopwords
        if current_word in set(stopwords.words('english')):
            continue

        try:
            total_count = sum(int(count) for current_word, count in group)
            print("{}{}{}".format(current_word, separator, total_count))
        except ValueError:
            # count was not a number, so silently discard this item
            print("nok")
            pass

if __name__ == "__main__":
    main()