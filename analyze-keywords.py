from collections import defaultdict
import os
import codecs
import re
# import string
# import unicodedata
import unidecode

os.chdir('/path/to/dictionaries/')

input_file_name = 'dict-en.dic'
output_file_name = 'podobne-en.txt'


def transform_keyword(keyword=''):
    transformed = keyword
    chars_to_replace = {'ł': 'l', 'ą': 'a', 'ę': 'e', 'ż': 'z', 'ź': 'z', 'ś': 's', 'ć': 'c', 'ó': 'o',
                        'Ł': 'l', 'Ą': 'a', 'Ę': 'e', 'Ż': 'z', 'Ź': 'z', 'Ś': 's', 'Ć': 'c', 'Ó': 'o'}
    for old, new in chars_to_replace.items():
        transformed = transformed.replace(old, new)

    # transformed = ''.join(x for x in unicodedata.normalize('NFKD', keyword) if x in string.ascii_letters)

    transformed = re.sub('[^a-zA-Z]', '', transformed)
    transformed = unidecode.unidecode(transformed)

    return transformed


f = codecs.open(input_file_name, 'r', 'utf-8')
total_count = 0

similar_keywords = defaultdict(list)

for keyword in f:
    plain_keyword = keyword.replace('\n', '')
    transformed_keyword = transform_keyword(plain_keyword)
    print(plain_keyword, '\t', transformed_keyword)
    total_count += 1

    similar_keywords[transformed_keyword].append(plain_keyword)

f.close()

print()
out = codecs.open(output_file_name, 'w', 'utf-8')
for transformed, keywords in similar_keywords.items():
    if len(keywords) > 1:
        for keyword in keywords:
            print(keyword)
            out.write(keyword + '\n')
        print()
        out.write('\n')

print('Total count:', total_count)
out.close()