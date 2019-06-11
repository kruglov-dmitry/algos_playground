#
#   https://leetcode.com/problems/word-pattern/
#


def word_pattern(pattern, input_string):
    """
    :type pattern: str
    :type input_string: str
    :rtype: bool
    """

    words = input_string.split()

    if len(words) != len(pattern):
        return False

    idx = 0
    dct = {}
    v = {}

    for x in pattern:
        if x not in dct:

            if words[idx] in v:
                return False

            dct[x] = words[idx]
            v[words[idx]] = x
        else:

            if words[idx] not in v:
                return False

            if x != v[words[idx]]:
                return False
        idx += 1

    return True
