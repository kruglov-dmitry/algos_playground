# coding=utf-8
#
#   https://leetcode.com/problems/majority-element/
#
# Given an array of size n, find the majority element.
# The majority element is the element that appears more than ⌊ n/2 ⌋ times.
# You may assume that the array is non-empty and the majority element always exist in the array.


def majority_element(nums):
    el = cnt = 0
    for entry in nums:
        if entry == el:
            cnt += 1
        elif cnt == 0:
            cnt, el = 1, entry
        else:
            cnt -= 1

    return el

# nums = [-1, 1, 1, 1, 2, 1]  # 1
# nums = [32,41,21,29,7,53,97,76,71,53,53,53,72,53,53,14,22,53,67,53,53,53,54,98,53,46,53,53,62,53,76,20,60,53,31,53,53,53,95,27,53,53,53,53,36,59,40,53,53,64,53,53,53,21,53,51,53,53,2,53,53,53,53,53,50,53,53,53,23,88,3,53,61,19,53,68,53,35,42,53,53,48,34,54,53,75,53,53,50,44,92,41,71,53,53,82,53,53,14,53] # 53

nums = [2,2,1,1,1,2,2]
print majority_element(nums)