from collections import Counter

#
#   https://leetcode.com/problems/minimum-window-substring
#


def minimum_window_substring(s, t):
    ll = len(s)
    lll = len(t)
    if lll > ll:
        return ""

    counter = Counter(t)
    cur_counter = Counter()

    min_len = ll
    l, r = 0, ll
    seen = False

    start = 0
    for idx in xrange(ll):
        if s[idx] not in counter:
            continue

        cur_counter[s[idx]] += 1

        should_check = all(cur_counter.get(k, 0) >= counter.get(k)
                           for k in counter)

        if not should_check:
            continue

        seen = True

        while True:
            if s[start] in cur_counter:
                cur_counter[s[start]] -= 1

                if 1 + cur_counter[s[start]] == counter.get(s[start]):
                    cur_counter[s[start]] += 1
                    break

            start += 1
            if start >= idx:
                break

        cur_len = idx + 1 - start
        if 0 <= cur_len < min_len:
            min_len = cur_len
            l = start
            r = idx + 1

    if not seen:
        return ""
    else:
        return s[l:r]


# S = "ADOBECODEBANC"
# T = "ABDC"

S = "BCDAAQA"
T = "AQA"
# #
# S = "BCDAAQA"
# T = "ADQ"
# #
S = "BB"
T = "BB"
# #
# S = "BBB"
# T = "BB"
# #
# S = "ABC"
# T = "BA"
# #
# S = "ABC"
# T = "BC"

print minimum_window_substring(S, T)

