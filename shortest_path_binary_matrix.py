from collections import deque

#
#   https://leetcode.com/problems/shortest-path-in-binary-matrix/
#


def shortest_path_binary_matrix(grid):
    num_rows = len(grid)
    if not num_rows:
        return -1

    num_columns = len(grid[0])
    if not num_columns:
        return -1

    if grid[num_rows-1][num_columns-1] == 1 or grid[0][0] == 1:
        return -1

    q = deque()
    q.append((1, 0, 0))

    visited = {0, 0}

    shifts = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1)]

    while q:

        cur_cnt, cur_y, cur_x = q.popleft()

        if cur_y == num_rows - 1 and cur_x == num_columns - 1:
            return cur_cnt
        else:
            for x, y in shifts:
                x2 = cur_x + x
                y2 = cur_y + y
                if 0 <= x2 < num_columns and 0 <= y2 < num_rows and grid[y2][x2] != 1 and (y2, x2) not in visited:
                    q.append((cur_cnt+1, y2, x2))
                    visited.add((y2, x2))

    return -1


input1 = [[0,1],[1,0]]
input2 = [[0,0,0],[1,1,0],[1,1,0]]
input3 = [
    [0,0,0],
    [1,1,0],
    [1,1,1]
]

print shortest_path_binary_matrix(input3)
