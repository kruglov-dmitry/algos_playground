#
#   https://leetcode.com/problems/subarray-sum-equals-k
#


def solution(arr, target_sum):
    d = {}
    res, cur_sum = 0, 0

    for i, b in enumerate(arr):

        cur_sum += b

        if cur_sum == target_sum:
            res += 1

        if cur_sum - target_sum in d:
            res += d[cur_sum - target_sum]

        d[cur_sum] = d.get(cur_sum, 0) + 1

    return res

print solution([1,1,1], 2)
