# coding=utf-8
"""
Given two arrays:
    v1 = [1, 2]
    v2 = [3, 4, 5, 6]

We need to implement ZigzagIterator with following methods:
    has_next() - return whether iterator point to element
    next() - return current element if it exist

Example:
    sequential calls of next() will print elements of v1 and v2 in following order:
[1, 3, 2, 4, 5, 6]
"""


class ZigzagIterator:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

        self.l1 = len(v1)
        self.l2 = len(v2)

        self.cur_idx = 0
        self.last_first = True

    def has_next(self):
        return self.cur_idx < max(self.l1, self.l2)

    def next(self):
        if not self.has_next():
            return None

        if self.last_first:
            if self.cur_idx < self.l1:
                self.last_first = False
                if self.cur_idx >= self.l2:
                    prev = self.cur_idx
                    self.cur_idx += 1
                    return self.v1[prev]
                else:
                    return self.v1[self.cur_idx]
            elif self.cur_idx < self.l2:
                self.last_first = True
                prev = self.cur_idx
                self.cur_idx += 1
                return self.v2[prev]
        else:
            self.last_first = True
            prev = self.cur_idx
            self.cur_idx += 1
            if prev < self.l2:
                return self.v2[prev]
            else:
                return self.v1[prev]

# [1 2] [3] -> [1 3 2]

# [] [1 2 3]
# [1 2 3] []

# [1 2] [1 2 3 ]
# [1 2 3] [1 2]

# [1 2 3] [1 2 3]

#u = ZigzagIterator([2, 4, 10, 12, 34], [-1006])

u = ZigzagIterator([0, 67, 100], [-1006, 1, 13, 45, 29])

#u = ZigzagIterator([1, 2], [3, 4, 5])

while u.has_next():
    print u.next()
