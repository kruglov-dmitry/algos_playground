# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """

        ll = len(intervals)

        if ll < 2:
            return intervals

        res = []

        intervals.sort(key=lambda x: x.start)

        idx = 0

        cur_interval = intervals[idx]

        while idx < ll - 1:

            idx += 1

            if intervals[idx].start <= cur_interval.end:
                cur_interval.end = max(cur_interval.end, intervals[idx].end)
            elif cur_interval.end < intervals[idx].start:
                res.append(cur_interval)
                cur_interval = intervals[idx]

        res.append(cur_interval)

        return res
