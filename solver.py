import codecs
import random
import ngram_score as ns
import copy
lang_model = ns.ngram_score('./english/english_trigrams.txt')
file_ngrams = './ngrams/text4_3gram.txt'


encrypted_text = ""
cont = 0
with codecs.open(file_ngrams, 'r', 'utf-8') as f:
    for line in f:
        i, d = [func(x) for func, x in zip([str, float], line.strip().split('       	'))]
        encrypted_text += ' '+i
        if cont > 100 : break
        cont+=1
# encrypted_text = 'enie  wqen  enqz  enoh  fpbg  tbbs  gbpo  wnie  nivo  wnom  wopo  eqgo  poiy  lqso  zbgo  gbze  qmeb  smbw  wqll  lqfo  bmlh  giyo  ilzb  wnqcn  itbde  tbbsz  enopo  mbvol  hoipz  benop  enoqp  wbply  enbzo  wbdly  epden  bfeom  zebph  wpqeo  enozo  cbdly '

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


ref_score = -1000000
max_score = ref_score
t = 1.0
cooling_down = 0.9997

while True:
    new_key = shuffle(key)
    new_score = calc_score(new_key)
    if new_score > ref_score:
        if new_score > max_score:
            max_score = new_score
            print('temperature', t)
            print('POINTS', new_score)
            print('KEY', new_key)
            print(translate(cipher_alphabet, new_key, encrypted_words))
        key = new_key
        ref_score = new_score

    else:
        if random.random() < t:
            ref_score = new_score
            key = new_key
    t *= cooling_down