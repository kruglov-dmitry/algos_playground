#
#   https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
#


def helper(l, h, nums):
    def helper(l, h, nums):
        u = h - l
        if u < 2:
            return min(nums[l], nums[h])

        mid = l + u / 2 + u % 2
        if nums[l] < nums[h]:
            return helper(l, mid, nums)
        if nums[mid] > nums[l]:
            return helper(mid, h, nums)

        return helper(l, mid, nums)


def find_minimum_of_sorted_array(nums):
    if not nums:
        return 0

    return helper(0, len(nums) - 1, nums)


assert find_minimum_of_sorted_array([1, 2, 3]) == 1

assert find_minimum_of_sorted_array([3,4,5,1,2]) == 1

assert find_minimum_of_sorted_array([4,5,6,7,0,1,2]) == 0

assert find_minimum_of_sorted_array([3,0, 2]) == 0

assert find_minimum_of_sorted_array([3, 0, 1, 2]) == 0

assert find_minimum_of_sorted_array([]) == 0

assert find_minimum_of_sorted_array([123]) == 123

assert find_minimum_of_sorted_array([2, 1]) == 1