import random
import ngram_score as ns
import copy
import re
lang_model = ns.ngram_score('./english/english_trigrams.txt')

# to run it for text4
encrypted_text = open('./cipher/text4_translated.txt').readline()

# -----------------------------------
# to run it for text1/2/3 uncomment the following lines and change the path accordingly
# remove punctuations, normalize space
# encrypted_text = re.sub(r'[^a-z\s]', '', encrypted_text.lower())
# encrypted_text = re.sub(r'\s{2,}', ' ', encrypted_text.lower())
# ------------------------------------

encrypted_words = encrypted_text.split(' ')
cipher_alphabet = list(set(encrypted_text.replace(' ', '')))
key = 'abcdefghijklmnopqrstuwvxyz'


def calc_score(key):
    total = 0
    mapping = dict(zip(cipher_alphabet, key))
    for word in encrypted_words:
        decrypted_word = ''.join([mapping.get(l, '') for l in word])
        total += lang_model.score(decrypted_word)
    return total


def translate(cipher, key, crypted_words):
    mapping = dict(zip(cipher, key))
    return ' '.join([''.join([mapping.get(l, '') for l in word]) for word in crypted_words])


def shuffle(key):
    a = random.randint(0, len(key)-1)
    b = random.randint(0, len(key)-1)
    key_list = list(key)
    key_list[a], key_list[b] = key_list[b], key_list[a]
    return ''.join(key_list)


ref_score = -9999999
max_score = ref_score
t = 1.0
# the decrease factor of moving to a neighbour state
cooling_down = 0.9990
while True:
    new_key = shuffle(key)
    new_score = calc_score(new_key)
    if new_score > ref_score:
        if new_score > max_score:
            # save a new state
            max_score = new_score
            print('score: ', new_score)
            print('key: ', new_key)
            print(translate(cipher_alphabet, new_key, encrypted_words))
        key = new_key
        ref_score = new_score

    else:
        # move to a neighbouring state
        # the chance of moving to a neighbouring decreases as the process going on
        if random.random() < t:
            ref_score = new_score
            key = new_key
    t *= cooling_down
    if t < 0.0001:
        break
