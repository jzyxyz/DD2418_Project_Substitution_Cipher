from pycipher import SimpleSubstitution as SimpleSub
import random
import re
from ngram_score import ngram_score
import argparse
fitness = ngram_score('english_quadgrams.txt')  # load our quadgram statistics


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='substituition decipher for text file')
    parser.add_argument('--file', '-f', type=str,
                        required=True, help='path to the text file')

    arguments = parser.parse_args()
    return arguments


if __name__ == '__main__':
    arguments = parse_arguments()
    targetfile = open(arguments.file, 'r')
    cipher_text = targetfile.readline()
    normalized_cipher = re.sub(r'[^A-Z]', '', cipher_text.upper())
    maxkey = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    maxscore = -99e9
    parentscore, parentkey = maxscore, maxkey[:]
    print("Substitution Cipher solver, you may have to wait several iterations")
    print("for the correct result. Press ctrl+c to exit program.")
    # keep going until we are killed by the user
    i = 0
    while True:
        i = i+1
        random.shuffle(parentkey)
        deciphered = SimpleSub(parentkey).decipher(normalized_cipher)
        parentscore = fitness.score(deciphered)
        count = 0
        while count < 1000:
            a = random.randint(0, 25)
            b = random.randint(0, 25)
            child = parentkey[:]
            # swap two characters in the child
            child[a], child[b] = child[b], child[a]
            deciphered = SimpleSub(child).decipher(normalized_cipher)
            score = fitness.score(deciphered)
            # if the child was better, replace the parent with it
            if score > parentscore:
                parentscore = score
                parentkey = child[:]
                count = 0
            count = count+1
        # keep track of best score seen so far
        if parentscore > maxscore:
            maxscore, maxkey = parentscore, parentkey[:]
            print('\nbest score so far:', maxscore, 'on iteration', i)
            ss = SimpleSub(maxkey)
            print('    best key: '+''.join(maxkey))
            print('    plaintext: '+ss.decipher(normalized_cipher))
