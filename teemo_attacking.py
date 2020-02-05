#
#   https://leetcode.com/problems/teemo-attacking/
#


def teemo_attacking(timeSeries, duration):
    tot = 0
    if not timeSeries:
        return tot

    prev = timeSeries[0]
    ll = len(timeSeries)
    for idx in xrange(1, ll):
        cur = timeSeries[idx]
        if cur - prev >= duration:
            tot += duration
        else:
            tot += cur - prev

        prev = cur

    tot += duration

    return tot
