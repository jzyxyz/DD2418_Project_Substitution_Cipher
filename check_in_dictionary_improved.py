
def readDictionary(file):
    lexicon = {}
    with open(file, 'r', encoding="utf8", errors='replace') as f:
        for line in f:
            lexicon[line.strip()] = True
    return lexicon


def readText(file):
    return list(open(file, 'r', encoding='utf8').readline())


class Bad:
    def __init__(self, position, falsy, original, word):
        self.position = position
        self.falsy = falsy
        self.original = original
        self.word = word

    def format(self):
        obj = {}
        obj['position'] = self.position
        obj['falsy_char'] = self.falsy
        obj['true_char'] = self.original
        obj['word'] = self.word
        print(obj)


if __name__ == "__main__":
    dicfile = "./english/google10000english.txt"
    textfile = "./cipher/text4_solver.txt"
    original = './cipher/text4.txt'
    # original_list = list(open(original, 'r').readline())
    original_list = readText(original)
    lexicon = readDictionary(dicfile)
    # falsy_text_list = readText(textfile)
    falsy_text_list = list(input('enter text:'))
    # print(falsy_text_list)
    bad_words = []
    start = 0
    window_limit = 10

    while start < len(falsy_text_list):
        possible_boundry = []
        falsy_index = 0
        for j in range(1, window_limit):
            if start+j > len(falsy_text_list):
                break
            possible_word = ''.join(falsy_text_list[start:start+j])
            if possible_word not in lexicon:
                falsy_index = start+j
            else:
                possible_boundry.append(j)
                # print(''.join(falsy_text_list[start:start+j]))
        if len(possible_boundry) == 0:
            bw = Bad(position=start, falsy=falsy_index,
                     original=original_list[falsy_index], word=possible_word)
            bad_words.append(bw)
            start += 1
            # bw.format()
        elif len(possible_boundry) == 1:
            print(start, possible_boundry[0], ''.join(
                falsy_text_list[start:start+possible_boundry[0]]))
            start += possible_boundry[0]
            # print(start)
        else:
            longest_match_length = max(possible_boundry)
            print(start, longest_match_length+start, ''.join(
                falsy_text_list[start:start+longest_match_length]))
            start += longest_match_length

    for bw in bad_words:
        bw.format()
