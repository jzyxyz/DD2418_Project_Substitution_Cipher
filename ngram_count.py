from collections import defaultdict
import argparse
import os
from itertools import islice
import collections
import re
from functools import reduce


def generate_window(seq, n):
    "Returns a sliding window (of width n) over data from the iterable"
    "   s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...                   "
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield ''.join(result)
    for elem in it:
        result = result[1:] + (elem,)
        yield ''.join(result)


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='n_gram probs calculator for text file')
    parser.add_argument('--file', '-f', type=str,
                        required=True, help='path to the text file')
    parser.add_argument('--ngrams', '-n', type=int,
                        required=True, default=1, help='the n in ngram')

    arguments = parser.parse_args()
    return arguments


if __name__ == '__main__':
    arguments = parse_arguments()
    count = defaultdict(int)

    base = os.path.basename(arguments.file)
    targetfile = open(arguments.file, 'r')
    text = targetfile.readline().lower()
    text = re.sub(r'[\d]',
                  '', text).lower()
    text_list = list(text)
    targetfile.close()

    for n_gram in generate_window(text_list, arguments.ngrams):
        count[n_gram] += 1

    gramfile = open('./ngrams/' + os.path.splitext(base)
                    [0] + '_' + str(arguments.ngrams) + 'gram.txt', 'w')

    sorted_count = collections.OrderedDict(
        sorted(count.items(), key=lambda kv: kv[1], reverse=True))

    ngram_total_count = reduce(
        lambda acc, cur: acc + cur, sorted_count.values(), 0)

    for key in sorted_count:
        freq = sorted_count[key]/ngram_total_count
        # if freq > 0.0001:
        gramfile.write('{:10s}\t{:.4f}\n'.format(
            key, freq))

    gramfile.close()
