#
#   https://leetcode.com/problems/house-robber
#


def house_robber(nums):
    ll = len(nums)

    if ll == 0:
        return 0
    elif ll == 1:
        return nums[0]
    elif ll == 2:
        return max(nums)

    pre_prev = max(nums[0], nums[1])
    prev = max(nums[0] + nums[2], nums[1])

    for idx in xrange(3, ll):
        pre_prev, prev = prev, max(pre_prev + nums[idx], prev)

    return prev


inp1 = [3, 5, 1, 3, 4, 5, 1]

print house_robber(inp1)