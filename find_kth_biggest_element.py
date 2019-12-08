from heapq import heappop, heapify

#
#   https://leetcode.com/problems/kth-largest-element-in-an-array/
#


def find_kth_biggest_element(nums, k):
    for idx in xrange(len(nums)):
        nums[idx] = -nums[idx]
    heapify(nums)

    while True:
        res = heappop(nums)
        k -= 1
        if k == 0:
            return -res
