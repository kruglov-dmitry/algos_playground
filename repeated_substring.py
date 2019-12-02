#
#   https://leetcode.com/problems/repeated-substring-pattern/
#


def check(step, some_str, ll):

    for start in xrange(step, ll, step):
        if some_str[:step] != some_str[start:start + step]:
            return False

    return True


def repeated_substring_pattern(some_str):
    if not some_str:
        return False

    ll = len(some_str)

    first = some_str[0]

    step = 0
    for l in some_str[1:]:
        step += 1
        if l == first and ll % step == 0:
            success = True
            for start in xrange(step, ll, step):
                if some_str[:step] != some_str[start:start + step]:
                    success = False
                    break

            if success:
                return True

    return False

assert repeated_substring_pattern("aa") is True

assert repeated_substring_pattern("abac") is False

assert repeated_substring_pattern("") is False
assert repeated_substring_pattern("c") is False

assert repeated_substring_pattern("abab") is True

assert repeated_substring_pattern("aba") is False

assert repeated_substring_pattern("abcabcabcabc") is True

assert repeated_substring_pattern("abcab"
                                  "abcab") is True
