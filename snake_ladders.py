#
#   https://leetcode.com/problems/snakes-and-ladders/
#


def bfs(move, last):
    # idx, dice_counter
    queue = [(0, 0)]

    visited = set()
    visited.add((0, 0))

    num_dice_throw = 0

    while len(queue) > 0:

        idx, num_dice_throw = queue.pop(0)

        if idx == last:
            return num_dice_throw

        num_dice_throw += 1

        for didx in xrange(1, 7):

            new_idx = idx + didx

            if new_idx > last:
                break

            if move[new_idx] != -1:
                new_idx = move[new_idx] - 1

            if new_idx not in visited:
                queue.append((new_idx, num_dice_throw))
                visited.add(new_idx)

    return -1


def solution(board):
    max_y = len(board)

    if max_y == 0:
        return 0

    max_x = len(board[0])

    last = max_y * max_x

    move = [-1] * last

    y = max_y - 1
    x = 0
    idx = 0

    while True:
        if idx == last:
            break

        move[idx] = board[y][x]
        idx += 1

        if (y - max_y - 1) % 2 == 0:  # --->
            if x < max_x - 1:
                x += 1
            else:
                y = y - 1
                x = max_x - 1
        else:  # <---
            if x > 0:
                x -= 1
            else:
                y = y - 1
                x = 0

    return bfs(move, last - 1)


def run_tests():

    test_input = [
        [-1,-1],
        [-1, 3]
    ] # 1
    assert solution(test_input) == 1

    test_input = [
        [-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1],
        [-1,35,-1,-1,13,-1],
        [-1,-1,-1,-1,-1,-1],
        [-1,15,-1,-1,-1,-1]
    ]  # 4
    assert solution(test_input) == 4

    test_input = [
        [-1, -1, -1],
        [-1, 9, 8],
        [-1, 8, 9]
    ]   # 1
    assert solution(test_input) == 1

    test_input = [
        [-1, -1, -1],
        [-1, 7, 8],
        [-1, 8, 5]
    ]   # 2
    assert solution(test_input) == 2

    test_input = [
        [-1, 4, -1],
        [6, 2, 6],
        [-1, 3, -1]
    ]   # 2
    assert solution(test_input) == 2

    test_input = [
        [-1,-1],
        [-1,-1],
        [-1,-1],
        [-1,-1],
        [-1,-1],
        [-1,-1],
        [-1,-1],
        [-1,-1],
        [-1, 3]
    ]   # 3
    assert solution(test_input) == 3

    test_input = [
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, 3, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    ]   # 5
    assert solution(test_input) == 5

    test_input = [
        [-1,-1,27,13,-1,25,-1],
        [-1,-1,-1,-1,-1,-1,-1],
        [44,-1,8,-1,-1,2,-1],
        [-1,30,-1,-1,-1,-1,-1],
        [3,-1,20,-1,46,6,-1],
        [-1,-1,-1,-1,-1,-1,29],
        [-1,29,21,33,-1,-1,-1]
    ]   # 4
    assert solution(test_input) == 4

run_tests()
