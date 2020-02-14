#   Given matrix, an n x n square matrix of integers, let's define its 0-border as the union of its
#   leftmost and rightmost columns, as well as its top and bottom rows.
#   If we were to remove the matrix's 0-border, then the 0-border of the resulting matrix can be defined
#   as the 1-border of the original matrix. We can continue this way to define the 2-border, 3-border, etc.
#
#   For each k in [0, 1, ..., floor((n - 1) / 2)], your task is to sort the elements in each k-border
#   and place them in clockwise order, starting from the top-left corner.
#
#   https://leetcode.com/discuss/interview-question/434795/Border-sort
#


def border_sort(A):
    N = len(A)

    res = []
    for y in xrange(N):
        res.append([-100500]*N)

    for k in xrange(1 + (N-1) // 2):
        top = A[k][k:N-k]
        bottom = A[N-k-1][k:N-k]
        left, right = [], []
        for Y in xrange(k+1, N-k-1):
            left.append(A[Y][k])
            right.append(A[Y][N-k-1])

        border_sorted = sorted(top+bottom+left+right)

        #   N = 7
        #   7   6   5   4   3   2   1
        #   8   9   10  11  12  13  14
        #   15  16  17  18  19  20  21
        #   22  23  24  25  26  27  28
        #   29  30  31  32  33  34  35
        #   36  37  38  39  40  41  42
        #   43  44  45  46  47  48  49

        new_top = border_sorted[:N-2*k]
        new_right = border_sorted[N-2*k:2*N-4*k-2]
        new_bottom = border_sorted[2*N-4*k-2:3*N-6*k-2][::-1]
        new_left = border_sorted[3*N-6*k-2:][::-1]

        # Fill resulting rows \ columns
        idx = 0
        for X in xrange(k, N-k):
            res[k][X] = new_top[idx]
            res[N - k - 1][X] = new_bottom[idx]
            idx += 1
        idx = 0
        for Y in xrange(k+1, N - k - 1):
            res[Y][k] = new_left[idx]
            res[Y][N - k - 1] = new_right[idx]
            idx += 1

    return res


A = [
    [9,4],
    [6,8]
]
r = border_sort(A)
res = [
    [4,6],
    [9,8]
]
for Y, row in enumerate(res):
    for X, el in enumerate(row):
        assert el == r[Y][X]


A = [
    [-100,-100],
    [-100,-100]
]
r = border_sort(A)
res = [
    [-100,-100],
    [-100,-100]
]
for Y, row in enumerate(res):
    for X, el in enumerate(row):
        assert el == r[Y][X]

A = [
        [15,-66,-18,99],
        [-80,-36,90,-10],
        [-59,-37,82,-33],
        [-15,26,61,-2]
]
r = border_sort(A)
res = [
    [-80,-66,-59,-33],
    [99,-37,-36,-18],
    [61,90,82,-15],
    [26,15,-2,-10]
]
for Y, row in enumerate(res):
    for X, el in enumerate(row):
        assert el == r[Y][X]


A = [
    [7,     6,  5,  4,  3,  2,  1],
    [8,     9,  10, 11, 12, 13, 14],
    [15,    16, 17, 18, 19, 20, 21],
    [22,    23, 24, 25, 26, 27, 28],
    [29,    30, 31, 32, 33, 34, 35],
    [36,    37, 38, 39, 40, 41, 42],
    [43,    44, 45, 46, 47, 48, 49]
]
r = border_sort(A)

for row in r:
    print row
