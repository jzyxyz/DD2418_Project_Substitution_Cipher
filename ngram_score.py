
from math import log10


class ngram_score(object):
    def __init__(self, ngramfile, sep=' '):
        self.ngrams = {}
        for line in open(ngramfile):
            key, count = line.split(sep)
            self.ngrams[key] = int(count)
            self.L = len(key)
        self.N = sum(self.ngrams.values())
        for key in list(self.ngrams.keys()):
            self.ngrams[key] = log10(float(self.ngrams[key])/self.N)
        # smoothing
        self.floor = log10(0.01/self.N)

    def score(self, text):
        # getting the entropy of a file
        sc = 0
        ngrams = self.ngrams.__getitem__
        for i in range(len(text)-self.L+1):
            ngram = text[i:i+self.L].upper()
            if ngram in self.ngrams:
                sc += ngrams(ngram)
        else:
            sc += self.floor

        return sc
