#
#   https://leetcode.com/problems/friend-circles/
#
#   NOTE: another input format: Y, N instead of 1, 0
#


def dfs(temp, v, visited, friends):

    if visited[v]:
        return

    visited[v] = True
    temp.append(v)

    for idx, val in enumerate(friends[v]):
        if val == 'Y':
            dfs(temp, idx, visited, friends)


def friend_circles(friends):
    num_vertexes = len(friends)

    visited = []
    cc = []

    for i in range(num_vertexes):
        visited.append(False)

    for v in range(num_vertexes):
        if not visited[v]:
            temp = []
            dfs(temp, v, visited, friends)
            if temp:
                cc.append(temp)
    return len(cc)


def run_tests():
    input = [
        ['Y', 'Y', 'N', 'N'],
        ['Y', 'Y', 'Y', 'N'],
        ['N', 'Y', 'Y', 'N'],
        ['N', 'N', 'N', 'Y']
    ]       # answer is two

    input1 = [
        ['Y', 'N', 'N', 'N', 'N'],
        ['N', 'Y', 'N', 'N', 'N'],
        ['N', 'N', 'Y', 'N', 'N'],
        ['N', 'N', 'N', 'Y', 'N'],
        ['N', 'N', 'N', 'N', 'Y']
    ]       # answer is five

    input2 = [
        ['Y', 'Y', 'N'],
        ['Y', 'Y', 'N'],
        ['N', 'N', 'Y']
    ]       # answer is two

    input3 = [
        ['Y', 'Y', 'N'],
        ['Y', 'Y', 'Y'],
        ['N', 'Y', 'Y']
    ]       # answer is one

    assert friend_circles(input) == 2
    assert friend_circles(input1) == 5
    assert friend_circles(input2) == 2
    assert friend_circles(input3) == 1


run_tests()
