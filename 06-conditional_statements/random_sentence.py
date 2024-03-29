# adjectives from: http://www.enchantedlearning.com/wordlist/adjectives.shtml
# nouns from: http://www.talkenglish.com/vocabulary/top-1500-nouns.aspx
# verbs from: http://www.linguasorb.com/english/verbs/most-common-verbs/

import random
'''
adjectives are 1 word per line
nouns has a line format of 'word frequency type/types' where type is a comma seperated list in parenthesis
verbs file contains the 100 most common english verbs line format 'position verb simplepast pastparticiple'
verbs line example: '1 to be were been' NOTE: if using line.split() to keep [1] and [2] together
'''
file_names = {'nouns':'dirty_noun_list.txt', 'adjectives': 'clean_adjective_list.txt', 'verbs': 'dirty_verbs_list.txt'}
words = {'nouns': [], 'adjectives':[], 'verbs': []}
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
# opens a filename and returns a list containing the first word on each line
def read_data(file_name):
    res = []
    with open(file_name) as f:
        for line in f:
            if line.strip():
                tmp_words = line.split()
                if file_name == 'dirty_verbs_list.txt':
                    res.append(tmp_words[2])
                else:
                    res.append(tmp_words[0])
    return res

# takes each filename from the dict file_names and puts the words into the corresponding list in the dict 'words'
for k, v in file_names.items():
    words[k] = read_data(v)
'''
for noun in words['nouns']:
    print(noun)

for adjective in words['adjectives']:
    print(adjective)
'''

# returns a string of a random adjective + a random noun
def generate_group_names(amount):
    res = []
    for i in range(20):
        a = random.choice(words['adjectives'])
        n = random.choice(words['nouns'])
        temp = '{0} {1}'.format(a,n)
        res.append(temp)
    return res

# generates a random sentence
def generate_sentence():
    a = random.choice(words['adjectives'])
    n = random.choice(words['nouns'])
    v = random.choice(words['verbs'])
    p = None

    if a[0] in vowels:
        p = 'an'
    else:
        p = 'a'
    temp = '{0} {1} {2} {3}'.format(p, a, n, v)
    return temp


# generates a random sentence
def generate_sentence2():
    a = random.choice(words['adjectives'])
    n = random.choice(words['nouns'])
    v = random.choice(words['verbs'])+'s'
    p = None

    if a[0] in vowels:
        p = 'an'
    else:
        p = 'a'
    temp = '{0} {1} {2} {3}'.format(p, a, n, v)
    return temp



print(generate_sentence2())
