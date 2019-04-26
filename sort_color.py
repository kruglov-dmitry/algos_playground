#
#   https://leetcode.com/problems/sort-colors/
#
#   Aka dutch flag problem
#


def sort_colors(nums):
    i = 0
    j = 0
    max_len = len(nums) - 1

    while j <= max_len:
        if nums[j] == 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1
        elif nums[j] == 2:
            nums[max_len], nums[j] = nums[j], nums[max_len]
            max_len -= 1
        else:
            j += 1


input = [2, 0, 2, 1, 1, 0]

# input = [1,2,0]
# input = [1,0,2]

input = [1, 0, 1]
sort_colors(input)
print input