#
#   https://leetcode.com/problems/rabbits-in-forest
#


def rabbit_in_forest(answers):
    res = {}

    r = 0
    for e in answers:
        res[e] = res.get(e, 0) + 1

    for e in res:
        if e == 0:
            r += res[e]
        elif res[e] <= e + 1:
            r += 1 + e
        else:
            x = 1 + e
            r += x * (res[e] // x)
            if res[e] % x > 0:
                r += x

    return r


assert rabbit_in_forest([2,2,2]) == 3
assert rabbit_in_forest([2,2,2,2]) == 6
assert rabbit_in_forest([2,2,2,2,2]) == 6
assert rabbit_in_forest([2,2,2,2,2,2]) == 6
assert rabbit_in_forest([2,2,2,2,2,2,2]) == 9
assert rabbit_in_forest([2,2,2,2,2,2,2,2]) == 9
assert rabbit_in_forest([2,2,2,2,2,2,2,2,2]) == 9


assert rabbit_in_forest([0, 0, 1, 1, 1]) == 6

assert rabbit_in_forest([1, 1, 2]) == 5

assert rabbit_in_forest([10, 10, 10]) == 11

assert rabbit_in_forest([3, 2, 1]) == 9

assert rabbit_in_forest([0]) == 1

assert rabbit_in_forest([10]) == 11

assert rabbit_in_forest([]) == 0

assert rabbit_in_forest([1, 1, 1, 2, 2, 2, 2]) == 10

assert rabbit_in_forest([2, 1, 2, 2, 2, 2, 2, 2, 1, 1]) == 13

assert rabbit_in_forest([1,1,1,1]) == 4

assert rabbit_in_forest([0,1,0,2,0,1,0,2,1,1]) == 11
