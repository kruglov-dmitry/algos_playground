#
#   https://leetcode.com/problems/maximum-subarray
#   https://e-maxx.ru/algo/maximum_average_segment
#


def max_subarray(nums):
    f_max, s = 0, 0

    if nums:
        f_max = nums[0]

    for b in nums:
        s += b
        if s >= f_max:
            f_max = s

        if s < 0:
            s = 0

    return f_max
