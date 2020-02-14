#
#   https://leetcode.com/problems/random-pick-with-weight/
#
import random


class Solution(object):
    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.len = len(w)

        self.mapping = {}
        self.max = 0
        self.min = 10**5
        for idx, entry in enumerate(w):
            self.max += entry
            self.min = min(self.min, entry)
            self.mapping[self.max] = idx

        self.intervals = sorted(self.mapping.keys())

    def bin_search(self, some_val):

        l, r = 0, self.len-1

        if some_val <= self.intervals[l]:
            return l

        if some_val == self.intervals[r]:
            return r

        while l < r:
            if r - 1 == l:
                if self.intervals[l] > some_val:
                    return l
                return r

            m = l + (r-l) // 2

            if self.intervals[m] > some_val:
                r = m
            elif self.intervals[m] < some_val:
                l = m
            else:   # self.intervals[m] == some_val
                return m

    def pickIndex(self):
        """
        :rtype: int
        """
        cur_val = random.randint(1, self.max)
        interval_idx = self.bin_search(cur_val)

        return self.mapping[self.intervals[interval_idx]]


w = [5]
s = Solution(w)
cnt = {}
for _ in xrange(1000):
    ii = s.pickIndex()
    cnt[ii] = cnt.get(ii, 0) + 1
print cnt


w = [5, 1, 9, 4, 1]
s = Solution(w)
cnt = {}
for _ in xrange(1000):
    ii = s.pickIndex()
    cnt[ii] = cnt.get(ii, 0) + 1
print cnt

w = [1, 1, 1, 1, 1, 1]
s = Solution(w)
cnt = {}
for _ in xrange(1000):
    ii = s.pickIndex()
    cnt[ii] = cnt.get(ii, 0) + 1
print cnt


w = [4, 2]
s = Solution(w)
cnt = {}
for _ in xrange(1000):
    ii = s.pickIndex()
    cnt[ii] = cnt.get(ii, 0) + 1
print cnt

w = [1, 1, 10]
s = Solution(w)
cnt = {}
for _ in xrange(1000):
    ii = s.pickIndex()
    cnt[ii] = cnt.get(ii, 0) + 1
print cnt