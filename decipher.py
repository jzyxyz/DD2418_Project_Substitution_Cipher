import re
from collections import defaultdict
LANG_LETTER_BY_FREQ = ["E", "T", "A", "O", "I", "N", "S", "R", "H", "L", "D",
                       "C", "U", "M", "F", "G", "P", "W", "Y", "B", "V", "K", "J", "X", "Z", "Q"]
LANG_LETTER_BY_FREQ = [item.lower() for item in LANG_LETTER_BY_FREQ]
ALPHABET_SIZE = len(LANG_LETTER_BY_FREQ)

LEFT_WINDOW = 1
RIGHT_WINDOW = 1

LEXICON = ['of', 'to', 'in', 'it', 'is', 'be', 'as', 'at', 'so', 'we', 'he',
           'by', 'or', 'on', 'do', 'if', 'me', 'my', 'up', 'an', 'go', 'no',
           'the', 'and', 'for', 'are', 'but', 'not', 'you', 'all', 'any', 'can', 'had', 'her',
           'was', 'one', 'our', 'out', 'day', 'get', 'has', 'him', 'his', 'how',
           'man', 'new', 'now', 'old', 'see', 'two', 'way', 'who', ]

PRIORITY = {}
for idx in range(len(LEXICON)):
    PRIORITY[LEXICON[idx]] = idx

# This contains the candidates for the Nth most frequent letter
# the most frequent can be on of         ['E', 'T']
# the second most frequent can be one of ['E', 'T', 'A']
# the third most frequent can be one of  ['E', 'T', 'A', 'O']
# ...
CANDIDATES = defaultdict(lambda: [])
candidates = defaultdict(lambda: [])

# mapping from encrypted letter to real letter
translation = defaultdict(lambda: '')
reverse_translation = defaultdict(lambda: '')


for idx in range(ALPHABET_SIZE):
    left = idx - LEFT_WINDOW if idx >= LEFT_WINDOW else 0
    right = idx + RIGHT_WINDOW if idx <= ALPHABET_SIZE - RIGHT_WINDOW else ALPHABET_SIZE
    CANDIDATES[idx] = LANG_LETTER_BY_FREQ[left:right]
    # print(CANDIDATES[idx])


def build_candidates():
    # build candidate list for every letter in the encrypted file
    i = 0
    for line in open('./ngrams/text1_1gram.txt', 'r').readlines():
        letter, freq = line.split()
        candidates[letter] = CANDIDATES[i]
        i += 1


def determine_a_and_i():
    lines = open('./tokens/text1_token_len1.txt', 'r').readlines()
    letter, freq = lines[0].split()
    translation[letter] = 'a'
    reverse_translation['a'] = letter
    letter, freq = lines[1].split()
    translation[letter] = 'i'
    reverse_translation['i'] = letter


def read_len2_token():
    lines = open('./tokens/text1_token_len2.txt', 'r').readlines()
    return [line.split()[0] for line in lines]


def read_len3_token():
    lines = open('./tokens/text1_token_len3.txt', 'r').readlines()
    return [line.split()[0] for line in lines]


build_candidates()
determine_a_and_i()
len2_tokens = read_len2_token()
len3_tokens = read_len3_token()

for el in translation:
    len2_tokens = [re.sub(r'(?<!<)%s(?!>)' % el, '<{}>'.format(
        translation[el]), tk) for tk in len2_tokens]

for tk in len2_tokens:
    if '<' in tk:
        decrpyted_letter = re.findall(r'(?<=<)[a-z](?=>)', tk)[0]
        encrypted_letter = re.findall(r'(?<!<)[a-z](?!>)', tk)[0]
        for cddt in candidates[encrypted_letter]:
            #     print(tk.replace(encrypted_letter, cddt))
            potential_word = decrpyted_letter + cddt
            if potential_word in LEXICON and decrpyted_letter not in translation:
                    translation[encrypted_letter] = cddt
                    reverse_translation[cddt] = encrypted_letter

for lttr in translation:
    print('{} - {}'.format(lttr, translation[lttr]))
# for cddt in candidates[encrypted_letter]:
