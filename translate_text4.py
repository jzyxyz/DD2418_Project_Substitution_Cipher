import re
text = open('./cipher/text4.txt').readline()

cleaned_text = re.sub(r'[\d]+', '', text)
cleaned_text = re.sub(r'[egq\'cyh,\\]+', ' ', text)

mapping = {
    '-': 'e',
    '?': 'g',
    '(': 'q',
    ';': 'h',
    ')': 'y',
    ':': 'c',
    '.': 'u'
}


for char in mapping.keys():
    print(char)
    cleaned_text = cleaned_text.replace(char, mapping[char])

print(cleaned_text)
