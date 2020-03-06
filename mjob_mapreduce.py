#!/usr/bin/env python3
"""Simple MrJob MapReduce"""


from mrjob.job import MRJob
import sys
import re

from os import listdir
from os.path import isfile, join

from mapper import main as mapper_main
from reducer import main as reducer_main


WORD_RE = re.compile(r"[\w']+")
DIR = sys.argv

files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
 
class WordCount(MRJob):
 
    def mapper(self, _, line):
        for word in WORD_RE.findall(line):
            yield (word.lower(), 1)
 
    # def combiner(self, word, counts):
    #     yield (word, sum(counts))
 
    def reducer(self, word, counts):
        yield (word, sum(counts))
 
if __name__ == '__main__':
    WordCount.run()
