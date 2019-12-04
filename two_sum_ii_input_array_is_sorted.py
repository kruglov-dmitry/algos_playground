#
#   https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
#


def two_sum_ii_input_array_is_sorted(numbers, target):
    low, hi = 0, len(numbers) - 1

    while low < hi:
        cur_sum = numbers[low] + numbers[hi]
        if cur_sum == target:
            return [low + 1, hi + 1]

        if cur_sum < target:
            low += 1
        else:
            hi -= 1


assert two_sum_ii_input_array_is_sorted([2,7,11,15], 9) == [1,2]
