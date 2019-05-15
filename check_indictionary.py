import re
import numpy as np

def readDictionary(file):
    results = dict()
    with open(file, 'r', encoding="utf8", errors='replace') as f:
        for line in f:
            results[line.strip()]=''
    return results

def readText(file):
    results = list()
    with open(file, 'r', encoding="utf8", errors='replace') as f:
        while True:
            c = f.read(1)
            results.append(c)
            if not c:
                break
    return results

def checkwords(reference, text, limit):
    vocabulary = "abcdefghijklmnopqrstuvwxyz"
    incorrect=dict()
    correct = np.zeros(len(vocabulary), dtype=int)
    init = 0
    while init<len(text):
        itter = init
        word=""
        temp = init
        while itter < (limit+init) and  itter<len(text) :
            candidate = "".join(text[init:itter])
            if candidate in reference:
                if len(candidate)> len(word):
                    word = candidate
                    temp = itter
            itter += 1
        if len(word)>0:
            init = temp
            print(word)
            for k in word:
                correct[vocabulary.index(k)] += 1
        else:
            incorrect[init]=text[init]
            #print(incorrect)
            init+=1
    return correct, incorrect


if __name__ == "__main__":
    dicfile = "./english/google10000english.txt"
    textfile = "./cipher/text4_solver.txt"
    dictionary = readDictionary(dicfile)
    textlist = readText(textfile)
    correct_distribution, posible_bad = checkwords(dictionary, textlist,10)
    print("this is the number of letters found in the correct words:\n", correct_distribution,
          "\n Position of posible incorrect letter and the letter found", posible_bad)
