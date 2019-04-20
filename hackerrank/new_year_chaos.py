#
#   https://www.hackerrank.com/challenges/new-year-chaos/problem
#   TLDR; count number of swaps for valid _partially sorted_ random access array
#


def number_of_bribes(state):
    n = len(state)

    for idx in xrange(n):
        if state[idx] - idx - 1 > 2:
            print("Too chaotic")
            return

    # insertion sort with swap counting
    cnt = 0
    i = 1
    while i < n:
        j = i
        while j > 0 and state[j - 1] > state[j]:
            state[j], state[j - 1] = state[j - 1], state[j]
            cnt += 1
            j -= 1
        i += 1

    print(cnt)


# test1 = [2, 1, 5, 3, 4]           # 3
# test2 = [2, 5, 1, 3, 4]           # Too chaotic
# test3 = [1, 2, 3, 4, 6, 5, 8, 7]  # 2
test4 = [1, 2, 5, 3, 7, 8, 6, 4]    # 7


number_of_bribes(test4)
