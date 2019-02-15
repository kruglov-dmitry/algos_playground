import sys
import os
import string
from collections import defaultdict

#
# Index write every word in a new line, in alphabetical order, that occurs in the textfile.
# After each word display in which line in the original textfile did the word appear.
#

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python file_indexing.py [path-to-file]")
        exit(0)

    file_name = sys.argv[1]
    index_file_name = "{fn}-index.txt".format(fn=os.path.splitext(file_name)[0])

    res = defaultdict(list)

    first_capitalized = defaultdict(list)

    with open(file_name, 'r') as src:
        for idx, line in enumerate(src):
            words = line.translate(None, string.punctuation).split()
            if not words:
                continue
            first_capitalized[words[0]].append(idx+1)
            for w in words[1:]:
                res[w].append(idx+1)

    #
    #       NOTE: In ambiguous cases, without dictionary, save first words with capital letters
    #
    for cap_word in first_capitalized:
        w = cap_word.lower()
        if w in res:
            for idx in first_capitalized[cap_word]:
                res[w].append(idx)
        else:
            for idx in first_capitalized[cap_word]:
                res[cap_word].append(idx)

    lower_words = sorted([x for x in res.keys() if x.islower()])
    upper_words = sorted([x for x in res.keys() if not x.islower()])

    with open(index_file_name, 'w') as dst:
        for word in lower_words + upper_words:
            line = word + " " + ','.join(map(str, res[word])) + "\n"
            dst.write(line)