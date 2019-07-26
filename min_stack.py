#
#   https://leetcode.com/problems/min-stack/
#

class MinStack:
    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, elem):
        self.stack.append(elem)

        if self.mins:
            self.mins.append(min(self.mins[-1], elem))
        else:
            self.mins.append(elem)

    def pop(self):
        if self.stack:
            self.stack.pop()
            self.mins.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]
        return None

    def get_min(self):
        if self.mins:
            return self.mins[-1]
        return None


u = MinStack()

for x in [-2, 0, -3]:
    u.push(x)

print u.get_min()
u.pop()
print u.top()
print u.get_min()
