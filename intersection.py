#
#   https://leetcode.com/problems/intersection-of-two-arrays
#


def intersection(nums1, nums2):
    nums1.sort()
    nums2.sort()

    idx1 = 0

    res = set()
    idx2 = 0

    l1 = len(nums1)
    l2 = len(nums2)

    while idx1 < l1 and idx2 < l2:
        if nums1[idx1] < nums2[idx2]:
            while idx1 < l1 and nums1[idx1] < nums2[idx2]:
                idx1 += 1
        elif nums2[idx2] < nums1[idx1]:
            while idx2 < l2 and nums2[idx2] < nums1[idx1]:
                idx2 += 1
        else:
            res.add(nums2[idx2])
            idx1 += 1
            idx2 += 1

    return list(res)