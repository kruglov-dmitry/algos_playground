#
#   https://leetcode.com/problems/climbing-stairs/
#


def climbing_stairs(n):
    if n < 2:
        return n

    pre_prev = 1
    prev = 2

    for idx in xrange(2, n):
        pre_prev, prev = prev, pre_prev + prev

    return prev
