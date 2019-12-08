#
#   https://leetcode.com/problems/daily-temperatures/
#


def daily_temperatures(T):
    ll = len(T)
    if not ll:
        return T

    res = [0] * ll

    stack = []

    for idx in xrange(ll-1, -1, -1):
        cnt = 0
        while stack:
            if stack[-1][0] > T[idx]:
                cnt = stack[-1][1] - idx
                break
            stack.pop()

        res[idx] = cnt

        stack.append((T[idx], idx))

    return res


# , your output should be [ 1,   1, 4,  2,  1,  1,  0,  0]
print daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73])
