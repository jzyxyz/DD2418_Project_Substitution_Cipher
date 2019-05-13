'''
Allows scoring of text using n-gram probabilities
17/07/12
'''
from math import log10
import collections



class ngram_score(object):
    def __init__(self, ngramfile, sep=' '):
        ''' load a file containing ngrams and counts, calculate log probabilities '''
        self.ngrams = {}
        for line in open(ngramfile, 'r').readlines():
            key, count = line.split(sep)
            self.ngrams[key] = int(count)
        self.L = len(key)
        self.N = sum(self.ngrams.values())
        # calculate log probabilities
        for key in list(self.ngrams.keys()):
            self.ngrams[key] = log10(float(self.ngrams[key])/self.N)
            # self.ngrams[key] = self.ngrams[key] / sum
        self.floor = log10(0.01/self.N)

    def score(self, text):
        ''' compute the score of text '''
        score = 0
        ngrams = self.ngrams.__getitem__
        for i in range(len(text)-self.L+1):
            if text[i:i+self.L] in self.ngrams:
                score += ngrams(text[i:i+self.L])
            else:
                score += self.floor
        return score
    
    def print(self):
        sorted_dict = collections.OrderedDict(
        sorted(self.ngrams.items(), key=lambda kv: kv[1], reverse=True))
        for ng in self.ngrams:
            print('{} {:.5f}'.format(ng, self.ngrams[ng]))

ngs = ngram_score('english_nigrams.txt')
ngs.print()
