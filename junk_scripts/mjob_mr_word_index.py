#!/usr/bin/env python3
"""Simple MrJob MapReduce"""

from mrjob.job import MRJob
from string import punctuation
import re
import pprint
import datetime
import nltk
from nltk.corpus import stopwords


# WORD_RE = re.compile(r"[\w']+")
 
class WordIndex(MRJob):
 
    def mapper(self, _, line):
        for word in line.translate(str.maketrans('', '', punctuation)).split():
            # if is a stopword, ignore
            if word.lower() not in stopwords.words('english'):
                yield (word.lower(), 1)

    # def combiner(self, word, counts):
    #     yield (word, sum(counts))
 
    # def reducer(self, word, counts):
    #     try:
    #         yield (word, sum(counts))
    #     except TypeError as e:
    #         pprint.pprint({'word:': word, 'value': counts})
    #         pass
 
if __name__ == '__main__':
    # start_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    WordIndex.run()

    # end_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    # pprint.pprint({'Started at:': start_time, 'Ended at:': end_time})
 