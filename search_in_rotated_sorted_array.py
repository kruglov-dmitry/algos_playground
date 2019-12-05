#
#   https://leetcode.com/problems/search-in-rotated-sorted-array/
#


def helper(l, h, nums, target):
    idx = h - l
    if idx < 2:
        if target == nums[l]:
            return l
        elif target == nums[h]:
            return h
        return -1

    mid = h - idx / 2 - idx % 2
    if nums[mid] == target:
        return mid

    if target < nums[mid]:
        if target < nums[l] < nums[mid]:
            return helper(mid, h, nums, target)

        return helper(l, mid, nums, target)

    if nums[mid] < target <= nums[h]:
        return helper(mid, h, nums, target)

    if nums[l] < nums[mid]:
        return helper(mid, h, nums, target)

    return helper(l, mid, nums, target)

def search_in_rotated_sorted_array(nums, target):
    l, h = 0, len(nums) - 1
    if h < 0:
        return -1
    return helper(l, h, nums, target)


assert search_in_rotated_sorted_array([0,1,2,4,5,6,7], 0) == 0

assert search_in_rotated_sorted_array([4,5,6,7,0,1,2], 0) == 4

assert search_in_rotated_sorted_array([4,5,6,7,0,1,2], -1) == -1

assert search_in_rotated_sorted_array([7,8,9, 0, 1, 2,3,4,5,6], 0) == 3

assert search_in_rotated_sorted_array([], 0) == -1

assert search_in_rotated_sorted_array([1, 0], 0) == 1

assert search_in_rotated_sorted_array([0, 1, 2], 2) == 2

assert search_in_rotated_sorted_array([2, 1, 0], 1) == 1

assert search_in_rotated_sorted_array([3,5,1], 3) == 0

assert search_in_rotated_sorted_array([5,1,3], 5) == 0

assert search_in_rotated_sorted_array([4,5,6,7,0,1,2], 0) == 4

assert search_in_rotated_sorted_array([5,1,3], 3) == 2

assert search_in_rotated_sorted_array([5,1,3], 1) == 1

assert search_in_rotated_sorted_array([4,5,6,7,8,1,2,3], 8) == 4
