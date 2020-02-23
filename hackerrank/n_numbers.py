#
#   Given a number N put all elements from 1 to N in array in following order
#   1,3, ..., 4, 2
#   Time: O(N)
#   Space: O(1)
#


def n_numbers(N):
    if N < 1:
        return []

    res = [0] * N

    prev = 0
    for idx in xrange(N//2):
        res[idx] = prev + 1
        res[N - 1 - idx] = res[idx] + 1

        prev = res[N - 1 - idx]

    if N % 2:
        res[N//2] = N

    return res


N = 4
assert [1, 3, 4, 2] == n_numbers(N)

N = 5
assert [1, 3, 5, 4, 2] == n_numbers(N)

N = 1
assert [1] == n_numbers(N)

N = 10
assert [1, 3, 5, 7, 9, 10, 8, 6, 4, 2] == n_numbers(N)
