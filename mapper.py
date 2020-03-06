#!/usr/bin/env python3
"""A more advanced Mapper, using Python iterators and generators."""

import sys
from string import punctuation

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 


def read_input(file):
    for line in file:
        # split the line into words
        # filtered_line = get_stop_words_filtered(line)
        yield line.translate(str.maketrans('', '', punctuation)).split()


def remove_gutenberg_disclaimers(file_text):
    """Remove Gutenbeng.org disclaimers from his books"""
    pass


def get_stop_words_filtered(sentence = "This is a sample sentence, showing off the stop words filtration."):
    """Remove english stop words from the sentence returning a new filtered sentence"""
    # @todo: refatotor to improve performance
    try:
        stop_words = set(stopwords.words('english')) 
        word_tokens = word_tokenize(sentence)
    except LookupError as e:
        print('-' * 12)
        pprint.pprint(e)
        print('-' * 12)
        print('Baixando biblioteca punkt da lib NTLK')
        nltk.download('punkt')

    filtered_list = [w for w in word_tokens if not w in stop_words] 
    filtered_sentence = ''
    for word in filtered_list:
        filtered_sentence += ' ' + word
    
    return filtered_sentence


def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_input(sys.stdin)
    for words in data:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        for word in words:
            print('{}{}{}'.format(word, separator, 1))

if __name__ == "__main__":
    main()