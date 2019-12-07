#
#   https://leetcode.com/problems/powerful-integers/
#


def powerful_integer(x, y, bound):

    max_i = 1
    res = 1
    cache_x = {0: 1}
    if x > 1:
        while res <= bound:
            res *= x
            cache_x[max_i] = res
            max_i += 1

    max_j = 1
    res = 1
    cache_y = {0: 1}
    if y > 1:
        while res <= bound:
            res *= y
            cache_y[max_j] = res
            max_j += 1

    res = set()
    for i in xrange(max_i):
        for j in xrange(max_j):
            cur = cache_x[i] + cache_y[j]
            if cur <= bound:
                res.add(cur)

    return res


powerful_integer(2, 3, 10)

powerful_integer(2, 3, 1)

powerful_integer(2, 3, 2)

powerful_integer(2, 1, 10)

powerful_integer(2, 0, 10)
