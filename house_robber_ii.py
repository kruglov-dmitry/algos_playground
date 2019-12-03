#
#   https://leetcode.com/problems/house-robber-ii/
#


def house_robber_ii(nums):
    if not nums:
        return 0

    ll = len(nums)

    if ll < 4:
        return max(nums)

    def rob(start_idx, end_idx):
        pre_prev = max(nums[start_idx], nums[start_idx+1])
        prev = max(nums[start_idx+1], nums[start_idx] + nums[start_idx+2])

        for idx in xrange(start_idx+3, end_idx):
            pre_prev, prev = prev, max(prev, pre_prev + nums[idx])

        return prev

    return max(rob(1, ll), rob(0, ll-1))


assert house_robber_ii([1]) == 1

assert house_robber_ii([1, 2]) == 2

assert house_robber_ii([1, 2, 3]) == 3

assert house_robber_ii([1, 2, 3, 4]) == 6

assert house_robber_ii([1, 2, 3, 1]) == 4

assert house_robber_ii([1, 2, 3, 1, 0]) == 4

assert house_robber_ii([1, 2, 3, 1, 2]) == 5

assert house_robber_ii([1, 2, 2, 1, 1]) == 3

assert house_robber_ii([1, 2, 3, 4, 6]) == 9

assert house_robber_ii([1, 2, 3, 4, 6, 1]) == 10

assert house_robber_ii([10, 10, 10, 10, 10, 10]) == 30

assert house_robber_ii([10, 10, 10, 10, 10, 100]) == 120

assert house_robber_ii([10, 10, 10, 10, 10]) == 20

assert house_robber_ii([10, 10, 10, 10, 10, 10, 10]) == 30

assert house_robber_ii([1,3,1,3,100]) == 103
