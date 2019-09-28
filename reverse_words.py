#
#   https://leetcode.com/problems/reverse-words-in-a-string/
#


def reverse_words2(inp):
    w = []

    end_idx = len(inp) - 1
    word_start = False
    for idx in xrange(len(inp) - 1, -1, -1):
        if inp[idx].isspace():
            if word_start:
                w.append(inp[idx + 1:end_idx + 1])
                word_start = False
        elif not word_start:
            word_start = True
            end_idx = idx

    if word_start:
        w.append(inp[:end_idx + 1])

    return " ".join(w)


def reverse_words(s):
    w = []
    cur_word = []
    for l in xrange(len(s) - 1, -1, -1):
        if not s[l].isspace():
            cur_word.append(s[l])
        elif cur_word:
            w.append("".join(cur_word)[::-1])
            cur_word = []

    if cur_word:
        w.append("".join(cur_word)[::-1])

    return " ".join(w)


inp1 = "a good   example"
inp2 = "  hello world!  "
inp3 = "the sky is blue"

print reverse_words2(inp3), "!"
