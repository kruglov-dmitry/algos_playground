#
#   https://leetcode.com/problems/spiral-matrix/
#


def spiral_matrix(matrix):
    height = len(matrix)
    if not height:
        return []

    width = len(matrix[0])

    res = []
    min_x, min_y = 0, 0
    max_x, max_y = width, height
    while min_x < max_x and min_y < max_y:
        # top
        res += matrix[min_y][min_x:max_x]

        if min_y == max_y - 1:
            break

        # right
        for Y in xrange(min_y+1, max_y-1):
            res.append(matrix[Y][max_x-1])

        # bottom
        res += reversed(matrix[max_y - 1][min_x:max_x])

        if min_x == max_x - 1:
            break

        # left
        for Y in xrange(max_y-2, min_y, -1):
            res.append(matrix[Y][min_x])

        # increment + check exit condition
        min_x += 1
        max_x -= 1
        min_y += 1
        max_y -= 1

    return res


matrix = [
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
]
res = [1, 2, 3, 6, 9, 8, 7, 4, 5]
r = spiral_matrix(matrix)
assert len(res) == len(r)
for idx in xrange(len(res)):
    assert r[idx] == res[idx]


matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12]
]
res = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
r = spiral_matrix(matrix)
assert len(res) == len(r)


matrix = [
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8],
    [9, 10],
    [11, 12]
]
res = [1, 2, 4, 6, 8, 10, 12, 11, 9, 7, 5, 3]
r = spiral_matrix(matrix)
assert len(res) == len(r)

matrix = [
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12]
]
res = [1, 2, 3, 4, 5, 6, 12, 11, 10, 9, 8, 7]
r = spiral_matrix(matrix)
assert len(res) == len(r)


matrix = [
    [1, 2],
    [3, 4]
]
res = [1, 2, 4, 3]
r = spiral_matrix(matrix)
assert len(res) == len(r)

matrix = [
    [1],
    [2],
    [3],
    [4]
]
res = [1, 2, 3, 4]
r = spiral_matrix(matrix)
assert len(res) == len(r)


matrix = [
    [1, 2, 3, 4]
]
res = [1, 2, 3, 4]
r = spiral_matrix(matrix)
assert len(res) == len(r)


matrix = [
    [1, 2, 3, 4, 5, 6, 7],
    [8, 9, 10, 11, 12, 13, 14],
    [15, 16, 17, 18, 19, 20, 21],
    [22, 23, 24, 25, 26, 27, 28],
    [29, 30, 31, 32, 33, 34, 35],
    [36, 37, 38, 39, 40, 41, 42],
    [43, 44, 45, 45, 46, 47, 48],
]
print spiral_matrix(matrix)


print spiral_matrix([[]])