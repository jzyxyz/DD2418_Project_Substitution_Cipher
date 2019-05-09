from collections import defaultdict
import argparse
import os
from itertools import islice


def window(seq, n):
    "Returns a sliding window (of width n) over data from the iterable"
    "   s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...                   "
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result


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
    text_list = list(targetfile.readline())
    targetfile.close()

    if arguments.ngrams == 1:
        for char in text_list:
            count[char] += 1
    elif arguments.ngrams == 2:
        bigram_generator = window(text_list, 2)
        for bigram in bigram_generator:
            count[bigram] += 1
    elif arguments.ngrams == 3:
        trigram_generator = window(text_list, 3)
        for trigram in trigram_generator:
            count[trigram_generator] += 1

    gramfile = open('./ngrams/' + os.path.splitext(base)
                    [0] + '_' + arguments.ngrams + 'gram.txt', 'w')

    for key in count:
        gramfile.write('{}\t{:.4f}\n'.format(key, count[key]/len(text_list)))

    gramfile.close()
