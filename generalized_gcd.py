from collections import defaultdict

table = defaultdict(dict)


def gcd(first, second):
    if second in table and first in table[second]:
        return table[second][first]
    elif first in table and second in table[first]:
        return table[first][second]

    x, y = first, second

    while y:
        x, y = y, x % y

    table[second][first] = x
    table[first][second] = x
    return table[second][first]


def generalized_gcd(arr):
    ll = len(arr)
    if ll == 1:
        return arr[0]

    last_gcd = gcd(arr[0], arr[1])

    for idx in xrange(2, ll):
        last_gcd = gcd(arr[idx], last_gcd)

    return last_gcd
