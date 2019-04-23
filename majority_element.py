# coding=utf-8
#
#   https://leetcode.com/problems/majority-element-ii/
#
# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
# Note: The algorithm should run in linear time and in O(1) space.
#


def majority_element(nums):
    """
        Idea is to find the most frequent elements using pair of counters.
        If we see non-tracked element - we decrement counters,
        if any of counters is already zero - reset this counter for new element

        At the end - find out number of occurance resulted elements and compare with n / 3 threshold

    :param nums:
    :return:
    """
    l = len(nums)
    thrshld = l // 3 + 1

    first, second = None, None
    cnt1, cnt2 = 0, 0
    for entry in nums:
        if entry == first:
            cnt1 += 1
        elif entry == second:
            cnt2 += 1
        elif cnt1 == 0:
            first = entry
            cnt1 = 1
        elif cnt2 == 0:
            second = entry
            cnt2 = 1
        else:
            cnt1 -= 1
            cnt2 -= 1

    res = []

    if nums.count(first) >= thrshld:
        res.append(first)
    if nums.count(second) >= thrshld:
        res.append(second)

    return res


def majority_element_2(nums):
    """
    Scan array from start and end
    and count 3 most recently added uniq elements
    if there are new element - I will remove lest frequent from my scan list
    at the end I will analyse both counters and compare count with n/3 + 1

    :param nums: input array of integers
    :return: list of all elements that appear more than ⌊ n/3 ⌋ times
    """
    l = len(nums)
    if l < 3:
        return list(set(nums))

    min_num = l // 3 + 1
    cnt = {}
    rev_cnt = {}
    for i in xrange(l):
        if len(cnt) != 3 or nums[i] in cnt:
            cnt[nums[i]] = cnt.get(nums[i], 0) + 1
        else:
            # just overwrite min
            min_val = None
            min_cnt = None
            for k in cnt:
                if not min_val:
                    min_val = k
                    min_cnt = cnt[k]
                elif cnt[k] < min_cnt:
                    min_val = k
                    min_cnt = cnt[k]
            del cnt[min_val]
            cnt[nums[i]] = 1

        if len(rev_cnt) != 3 or nums[l - i - 1] in rev_cnt:
            rev_cnt[nums[l - i - 1]] = rev_cnt.get(nums[l - i - 1], 0) + 1
        else:

            # just overwrite min
            min_val = None
            min_cnt = None
            for k in rev_cnt:
                if not min_val:
                    min_val = k
                    min_cnt = rev_cnt[k]
                elif rev_cnt[k] < min_cnt:
                    min_val = k
                    min_cnt = rev_cnt[k]
            del rev_cnt[min_val]
            rev_cnt[nums[l - i - 1]] = 1
    res = []
    for k in cnt:
        if cnt[k] >= min_num:
            res.append(k)

    if not res:
        for k in rev_cnt:
            if rev_cnt[k] >= min_num:
                res.append(k)

    return res


nums = [3, 2, 3]    # [3]
# nums = [4, 3, 2, 3]    # [3]
# nums = [2, 5, 4, 3, 3, 5]    # []
nums = [1, 1, 1, 3, 3, 2, 2, 2]    # [1, 2]

# nums = [-1,100,2,100,100,4,100]   # [100]
# nums = [1, 2, 2, 3, 3, 4, 4, 5, 1, 1, 1, 1]     # [1]
# nums = [1, 2, 3, 4, 5, 1, 3, 1, 4, 1, 2, 1]     # [1]

# nums = [3, 4, 5, 1, 3, 3]

print majority_element_2(nums)
print majority_element(nums)