#
#   https://leetcode.com/problems/valid-anagram/
#
#   Given a pair of string s and t
#   check whether they are anagram of each other
#


def valid_anagram(s, t):
    d1 = {}
    d2 = {}

    for l in s:
        if l in d1:
            d1[l] += 1
        else:
            d1[l] = 1

    for l in t:
        if l in d2:
            d2[l] += 1
        else:
            d2[l] = 1

    for l in d1:
        if l not in d2:
            return False

        if d1[l] != d2[l]:
            return False

    for l in d2:
        if l not in d1:
            return False

        if d1[l] != d2[l]:
            return False

    return True
