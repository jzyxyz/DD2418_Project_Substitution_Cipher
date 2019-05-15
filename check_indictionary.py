import re


def readDictionary(file):
    results = list()
    with open(file, 'r', encoding="utf8", errors='replace') as f:
        for line in f:
            results.append(line.strip())
    return  results

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
    incorrect=dict()
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
        else:
            incorrect[init]=text[init-1]
            #print(incorrect)
            init+=1
    return incorrect


if __name__ == "__main__":
    dicfile = "./english/google10000english.txt"
    textfile = "./cipher/text4_solver.txt"
    dictionary = readDictionary(dicfile)
    textlist = readText(textfile)
    posible_bad = checkwords(dictionary, textlist,10)
    print(posible_bad)
