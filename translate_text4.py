import re




def translate(mapping_arr):
    print(mapping_arr)
    text = open('./cipher/text4.txt').readline()
    cleaned_text = re.sub(r'[\d]+', '', text)
 #   cleaned_text = re.sub(r'[egq\'cyh,\\]+', ' ', text)
    for char in mapping_arr.keys():
       # print(char)
        cleaned_text = cleaned_text.replace(char, mapping_arr[char])

    print(cleaned_text)
    return cleaned_text

if __name__ == "__main__":
    mapping = {
        '-': 'e',
        '?': 'g',
        '(': 'q',
        ';': 'h',
        ')': 'y',
        ':': 'c',
        '.': 'u'
    }
    translate(mapping)