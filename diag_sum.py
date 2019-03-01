DEBUG = False

#
#       Boring computations of sum of elements at i-th diagonal
#

input = [
    [0, 1, 0, 0],
    [1, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0]
]

#
#       Left to Right, Bottom-Up
#
# 0 - 0,3
# 1 - 0,2 + 1,3
# 2 - 0,1 + 1,2 + 2,3
# 3 - 0,0 + 1,1 + 2,2 + 3,3
# 4 - 1,0 + 2,1 + 3,2
# 5 - 2,0 + 3,1
# 6 - 3,0
#
# I < N - 1:
#   X: 0 to i + 1, ++
#   Y: N - i -1 to N, ++
#
# I > N - 1:
#   X: I - N + 1 to N, ++
#   Y: 0 to 2 * N - 1 - I - 1, ++

#
#       Left to Right, Top-Down
#
# 0 - 0,0
# 1 - 0,1 + 1,0
# 2 - 0,2 + 1,1 + 2,0
# 3 - 0,3 + 1,2 + 2,1 + 3,0
# 4 - 1,3 + 2,2 + 3,1
# 5 - 2,3 + 3,2
# 6 - 3,3
#
# I <= N - 1:
#   X: 0 to i + 1, ++
#   Y: i to 0, --
#
# I > N - 1:
#   X: I - N + 1 to N, ++
#   Y: N-1 to I - N + 1, --

input2 = [
    [40, 1, 100],
    [50, 25, 99],
    [100, 50, 35]
]

input3 = [
    [1, 1, 10, 3, 5],
    [0, 1, 2, -10, 2],
    [0, 0, 0, 1, 5],
    [10, 0, 5, 1, 1],
    [5, -5, 5, 0, 1]
]


def bottom_up(A):
    num_of_diags = len(A)
    l = 2 * num_of_diags - 1

    res = []

    for i in xrange(l):
        diag_sum = 0
        if i <= num_of_diags - 1:
            x = 0
            y = num_of_diags - i - 1
            if DEBUG:
                print "i", i
            while x < i + 1 and x < num_of_diags and y < num_of_diags:
                if DEBUG:
                    print "x:", x, "y:", y
                diag_sum += A[y][x]
                y += 1
                x += 1
        else:
            if DEBUG:
                print "i", i
            x = i - num_of_diags + 1
            y = 0
            while x < num_of_diags and y < 2 * num_of_diags - 1 - i:
                if DEBUG:
                    print "x:", x, "y:", y
                diag_sum += A[y][x]
                x += 1
                y += 1

        res.append(diag_sum)

    return res


def top_down(A):
    sz = len(A)
    num_of_diags = 2 * sz - 1

    res = []

    for i in xrange(num_of_diags):
        diag_sum = 0
        if i <= sz - 1:
            x = 0
            y = i
            if DEBUG:
                print "i", i
            while x < min(i + 1, sz) and y >= 0:
                if DEBUG:
                    print "x:", x, "y:", y
                diag_sum += A[y][x]
                y -= 1
                x += 1
        else:
            if DEBUG:
                print "i", i
            x = i - sz + 1
            y = sz - 1
            while x < sz and y >= i - sz + 1:
                if DEBUG:
                    print "x:", x, "y:", y
                diag_sum += A[y][x]
                x += 1
                y -= 1

        res.append(diag_sum)

    return res

#
#       Special cases when we have matrix with 0 & 1 only
#
#
#      input = [
#           [0, 1, 0, 0],
#           [1, 0, 0, 0],
#           [0, 0, 0, 1],
#           [0, 0, 1, 0]
#       ]
#
#       Can be compactly represented as:
#


input_repr = [1, 0, 3, 2]


def bottom_up_compact(arr):
    sz = len(arr)
    l = 2 * sz - 1

    res = []

    for i in xrange(l):
        diag_sum = 0
        if i <= sz - 1:
            x = 0
            y = sz - i - 1
            if DEBUG:
                print "i", i
            while x < i + 1 and x < sz and y < sz:
                if DEBUG:
                    print "x:", x, "y:", y
                if arr[y] == x:
                    diag_sum += 1
                y += 1
                x += 1
        else:
            if DEBUG:
                print "i", i
            x = i - sz + 1
            y = 0
            while x < sz and y < 2 * sz - 1 - i:
                if DEBUG:
                    print "x:", x, "y:", y
                if arr[y] == x:
                    diag_sum += 1
                x += 1
                y += 1

        res.append(diag_sum)

    return res


def top_down_compact(arr):
    sz = len(arr)
    num_of_diags = 2 * sz - 1

    res = []

    for i in xrange(num_of_diags):
        diag_sum = 0
        if i <= sz - 1:
            x = 0
            y = i
            if DEBUG:
                print "i", i
            while x < min(i + 1, sz) and y >= 0:
                if DEBUG:
                    print "x:", x, "y:", y
                if arr[y] == x:
                    diag_sum += 1
                y -= 1
                x += 1
        else:
            if DEBUG:
                print "i", i
            x = i - sz + 1
            y = sz - 1
            while x < sz and y >= i - sz + 1:
                if DEBUG:
                    print "x:", x, "y:", y
                if arr[y] == x:
                    diag_sum += 1
                x += 1
                y -= 1

        res.append(diag_sum)

    return res

# print bottom_up_compact(input_repr)
# print bottom_up(input)

# print top_down_compact(input_repr)
# print top_down(input)


# input = [
#     [0, 1, 0, 0],
#     [1, 0, 0, 0],
#     [0, 0, 0, 1],
#     [0, 0, 1, 0]
# ]
#
# 0,3 - 0
# 0,2; 1,3 - 1
# 0,1; 1,2; 2,3 - 2
# 0,0; 1,1; 2,2; 3,3 - 3
# 1,0; 2,1; 3,2 - 4
# 2,0; 3,1 - 5
# 3,0 - 6


def diag_num_bottom_up(A, x, y):
    n = len(A)

    if x < y:
        return n - 1 - (y - x)
    elif x > y:
        return n - 1 + (x - y)
    else:
        return n - 1

# print diag_num_bottom_up(input3, 2, 3)


# input = [
#     [0, 1, 0, 0],
#     [1, 0, 0, 0],
#     [0, 0, 0, 1],
#     [0, 0, 1, 0]
# ]
#
# 0,0 - 0
# 0,1; 1,0 - 1
# 0,2; 1,1; 2,0 - 2
# 0,3; 1,2; 2,1; 3,0 - 3
# 1,3; 2,2; 3,1 - 4
# 2,3; 3,2 - 5
# 3,3 - 6


def diag_num_top_down(A, x, y):
    return x + y


# input3 = [
#     [1, 1, 10, 3, 5],
#     [0, 1, 2, -10, 2],
#     [0, 0, 0, 1, 5],
#     [10, 0, 5, 1, 1],
#     [5, -5, 5, 0, 1]
# ]

print diag_num_top_down(input3, 2, 3)