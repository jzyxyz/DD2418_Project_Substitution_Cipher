from translate_text4 import translate
from random import sample

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



def compare_with_dictionary(falsy_text_list):
    dicfile = "./english/google10000english.txt"
   # textfile = "./cipher/text4_solver.txt"
    original = './cipher/text4.txt'
    # original_list = list(open(original, 'r').readline())
    original_list = readText(original)
    lexicon = readDictionary(dicfile)
    #falsy_text_list = readText(textfile)
    # print(falsy_text_list)
    bad_words = []
    start = 0
    window_limit = 10
    correct_letters = dict()
    while start < len(falsy_text_list):
        possible_boundry = []
        falsy_index = 0
        for j in range(1, window_limit):
            if start + j > len(falsy_text_list):
                break
            possible_word = ''.join(falsy_text_list[start:start + j])
            if possible_word not in lexicon:
                falsy_index = start + j
            else:
                possible_boundry.append(j)
                # print(''.join(falsy_text_list[start:start+j]))
        if len(possible_boundry) == 0 :
            bw = Bad(position=start, falsy=falsy_index,
                     original=original_list[falsy_index], word=possible_word)
            bad_words.append(bw)
            start += 1
            # bw.format()
        elif len(possible_boundry) == 1:
   #         print(start, possible_boundry[0], ''.join(
   #             falsy_text_list[start:start + possible_boundry[0]]))
            for i in range(start,start + possible_boundry[0]):
                correct_letters[original_list[i]]=falsy_text_list[i]
       #     [correct_letters.add(i) for i in falsy_text_list[start:start + possible_boundry[0]]]
            start += possible_boundry[0]
        else:
            longest_match_length = max(possible_boundry)
        #    print(start, longest_match_length + start, ''.join(
        #        falsy_text_list[start:start + longest_match_length]))
            for i in range(start,start + longest_match_length):
                correct_letters[original_list[i]]=falsy_text_list[i]
            start += longest_match_length

    return correct_letters, bad_words


def check_text(falsy_text_list):
    correct, incorrect = compare_with_dictionary(falsy_text_list)
    bad_words = dict()
    candidates = list("abcdefghijklmnopqrstuvwxyz")
    for bw in incorrect:
        if bw.original not in correct:
            bad_words[bw.original] = falsy_text_list[bw.position]
    print(correct, len(correct),'\n',bad_words, len(bad_words))
    for k,v in correct.items():
        if v in candidates:
            candidates.remove(v)
    return correct,bad_words,candidates


if __name__ == "__main__":
   # falsy_text_list = list(input('enter text:'))
    new_txt = "whatiseducation whatisthestudyofeducation throughoutyoureducationkyouwillhavestudiedarangeofsub ectsatbothprimaryandsecondarylevelzsomeofyouwillalsohavestudiedatfecollegesorinheinstitutionszyoumayalsohaveengagedinsomestudiesawayfromschoolskinyouthclubsksummerschemesandatvariousotherlocationszpriortoanyformaleducationalexperiencesininstitutionskyouwillnodoubthavelearnttowaljktaljkinteractwithothersinsocialsituationskandperhapsevenreadandwritezifyouwereeducatedinenglandkyouwillnodoubthaveattendedaprimaryschoolandasecondaryschoolwhereyouwillhavestudiedarangeofsub ects someyouwillhaveen oyedwhileotherslesssozyouwillhavehadexcellentinspiringteachersandotherswhoseimpactuponyouwasnotsopositivezyouhavenodoubt ocjeyedforpositionamongthoseyouattendedschoolwithkyourpeerszyounodoubtreceivedpunishmentsksomefairkothersnotkandattimesreceivedrewardsandpraisezyoumayhavereceivedhighlevelsofsupportfromyourfamilyorcarersorperhapsyouwerelefttodevelopyourowninterestineducationzinshortkyouhavereceivedaneducationandeveninthisshortintroductorytextwecanbegintoseethateducationisnotsolelyaboutthecontentofthesub ectsthatyoulearntbutinsteadismultifacetedandcomplexandinvolvesmuchmorethanthoseelementswhichmayimmediatelyspringtomindwhendiscussingitzthestudyofeducationkthereforekatfirstglancedifferssignificantlyfrommanyofthesub ectsyouwillhavestudiedbeforekinthatitexamineskindetailkaprocessasopposedtoasub ectareazthroughoutthisboojkyouwillfindarangeofissuesrelevanttothestudyofeducationzthelistisnotexhaustiveknorisdesignedtobesozthisisnotaboojthatwilltellyouhoweithertoteachorhowtolearnzinsteadkitwillraiseissuesthatwillenableyoutobegintounderstandthepowerandimportanceofeducationzitwillopenupide"
    falsy_text_list = list(new_txt)
    maxgood = 0
    best_candidate,best_subs, best_falty = [],{},{}
    while maxgood < 26:
        correct, incorrect, candidates = check_text(new_txt)
        good = len(correct)
        if good > maxgood:
            maxgood = good
            best_candidates = candidates
            best_subs = correct
            best_falty = incorrect
        chosen_candidates = sample(best_candidates, len(best_falty))
        new_mapping = best_subs
        cont = 0
        for k, v in best_falty.items():
            new_mapping[k] = chosen_candidates[cont]
            cont+=1
        new_txt = translate(new_mapping)