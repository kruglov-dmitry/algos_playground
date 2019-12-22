#
#   You are given a string that may contains `smile` with variable number of brackets:
#           :-(( or :-)))))
#   You have to write function that clean it out from smiles
#
#   a:-)()) => a())
#   :-(((abc:-() => abc)
#   a => a
#


def smile_eliminations(some_str):
    w_idx, r_idx = 0, 0

    ll = len(some_str)
    end = ll - 3

    while r_idx <= end:
        if some_str[r_idx] == ':' and some_str[r_idx+1] == '-' and some_str[r_idx+2] in [")", "("]:
            prev = some_str[r_idx+2]
            r_idx += 3
            while r_idx < ll and some_str[r_idx] == prev:
                r_idx += 1
        else:
            some_str[w_idx] = some_str[r_idx]

            w_idx += 1
            r_idx += 1

    # remainder
    for rr in xrange(r_idx, ll):
        some_str[w_idx] = some_str[rr]
        w_idx += 1

    print some_str[:w_idx]
    return some_str[:w_idx]


assert smile_eliminations(list("a:-)())")) == list("a())")
assert smile_eliminations(list(":-(((abc:-()")) == list("abc)")
assert smile_eliminations(list("a")) == list("a")
assert smile_eliminations(list("abc")) == list("abc")
assert smile_eliminations(list("abc:")) == list("abc:")
assert smile_eliminations(list(":-):-(")) == list("")
assert smile_eliminations(list(":-:-(")) == list(":-")
assert smile_eliminations(list(":-(((((")) == list("")
assert smile_eliminations(list("")) == list("")
assert smile_eliminations(list(":-))))))(:-((()a(bc:-:-)")) == list("()a(bc:-")
assert smile_eliminations(list("a:-)b:-(c")) == list("abc")
assert smile_eliminations(list(":-)ca")) == list("ca")
