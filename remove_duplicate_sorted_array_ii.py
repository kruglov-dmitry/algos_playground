#
#   https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
#


def remove_duplicate_sorted_array(nums):
    if not nums:
        return 0

    r, w = 1, 1

    was_dup = False
    while r < len(nums):
        if not was_dup and nums[r] == nums[r-1]:
            was_dup = True
        elif was_dup:
            was_dup = False
            while r < len(nums) and nums[r] == nums[r-1]:
                r += 1
            if r >= len(nums):
                break
        elif was_dup:
            was_dup = False

        nums[w] = nums[r]
        r += 1
        w += 1

    return w


assert remove_duplicate_sorted_array([1, 2, 3]) == 3

assert remove_duplicate_sorted_array([3]) == 1

assert remove_duplicate_sorted_array([1, 2, 2, 3]) == 4

assert remove_duplicate_sorted_array([1, 1, 1, 2, 2, 3]) == 5

assert remove_duplicate_sorted_array([0, 0, 1, 1, 1, 1, 2, 3, 3]) == 7

assert remove_duplicate_sorted_array([0, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 5, 6, 7, 8, 9]) == 13

assert remove_duplicate_sorted_array([]) == 0

assert remove_duplicate_sorted_array([0, 0, 1, 1]) == 4

assert remove_duplicate_sorted_array([0, 0, 1]) == 3

assert remove_duplicate_sorted_array([0, 1, 1, 1]) == 3

assert remove_duplicate_sorted_array([1, 1, 1]) == 2
