#
#   https://leetcode.com/problems/word-search/
#
#   Given a matrix with letter and word
#   Determine whether we can assemble a word moving only from
#   aligned cells in matrix
#


def dfs(board, y, x, word, H, W):
    if len(word) == 0:
        return True

    if y >= H or y < 0 or x >= W or x < 0:
        return False

    if word[0] != board[y][x]:
        return False

    prev = board[y][x]
    board[y][x] = '*'

    res = dfs(board, y + 1, x, word[1:], H, W) or \
          dfs(board, y, x + 1, word[1:], H, W) or \
          dfs(board, y, x - 1, word[1:], H, W) or \
          dfs(board, y - 1, x, word[1:], H, W)

    board[y][x] = prev

    return res


def leetcode_word_search(board, word):

    H = len(board)
    if H < 1:
        return False

    W = len(board[0])

    if H * W < len(word):
        return False

    d = {}
    for l in word:
        d[l] = d.get(l, 0) + 1

    for y in xrange(H):
        for x in xrange(W):
            if board[y][x] in d:
                d[board[y][x]] -= 1

    for l in d:
        if d[l] > 0:
            return False

    for y in xrange(H):
        for x in xrange(W):
            if board[y][x] == word[0]:
                if dfs(board, y, x, word, H, W):
                    return True

    return False


def tests():
    board = [["a"]]
    word = "a"
    assert leetcode_word_search(board, word) == True

    board = [["a","a"]]
    word = "aa"
    assert leetcode_word_search(board, word) == True

    board = [["a","a"]]
    word = "aaa"
    assert leetcode_word_search(board, word) == False

    board = [["a","b"],["c","d"]]
    word = "abdc"
    assert leetcode_word_search(board, word) == True

    board = [["a","b"],["c","d"]]
    word = "abcd"
    assert leetcode_word_search(board, word) == False

    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]

    assert leetcode_word_search(board, "ABCCED") == True
    assert leetcode_word_search(board, "SEE") == True
    assert leetcode_word_search(board, "ABCB") == False

    board = [
        ["A","B","C","E"],
        ["S","F","E","S"],
        ["A","D","E","E"]
    ]

    assert leetcode_word_search(board, "ABCESEEEFS") == True


tests()
