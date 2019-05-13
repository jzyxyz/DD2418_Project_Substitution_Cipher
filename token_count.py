from collections import defaultdict
import argparse
import os
from itertools import islice
import collections
import re
from functools import reduce


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='n_gram probs calculator for text file')
    parser.add_argument('--file', '-f', type=str,
                        required=True, help='path to the text file')
    parser.add_argument('--length', '-l', type=int,
                        required=True, help='length of token')

    arguments = parser.parse_args()
    return arguments


if __name__ == '__main__':
    arguments = parse_arguments()
    count = defaultdict(int)

    base = os.path.basename(arguments.file)
    targetfile = open(arguments.file, 'r')
    text = targetfile.readline().lower()
    text = re.sub(r'[^a-z\s]',
                  '', text).lower()
    text_list = text.split()
    print(len(text_list))
    targetfile.close()

    match_length = list(
        filter(lambda t: len(t) == arguments.length, text_list))
    print(len(match_length))

    for token in match_length:
        count[token] += 1

    gramfile = open('./tokens/' + os.path.splitext(base)
                    [0] + '_token_len' + str(arguments.length) + '.txt', 'w')

    sorted_count = collections.OrderedDict(
        sorted(count.items(), key=lambda kv: kv[1], reverse=True))

    total_count = reduce(
        lambda acc, cur: acc + cur, sorted_count.values(), 0)

    for key in sorted_count:
        freq = sorted_count[key]/total_count
        if freq > 0.011:
            gramfile.write('{:10s}\t{:.4f}\n'.format(
                key, freq))

    gramfile.close()
