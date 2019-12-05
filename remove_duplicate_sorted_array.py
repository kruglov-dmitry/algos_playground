#
#   https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/
#


def remove_duplicate_sorted_array(nums):
    if not nums:
        return 0

    r, w = 1, 1

    while r < len(nums):
        while r < len(nums) and nums[r] == nums[r - 1]:
            r += 1
        if r >= len(nums):
            break

        nums[w] = nums[r]
        r += 1
        w += 1

    return w
