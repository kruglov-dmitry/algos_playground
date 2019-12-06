#
#   https://leetcode.com/problems/merge-sorted-array/
#


def merge_two_sorted_array(nums1, m, nums2, n):
    w = len(nums1) - 1

    first = m - 1
    second = n - 1

    while w > -1:
        if first < 0:
            while second >= 0:
                nums1[w] = nums2[second]
                second -= 1
                w -= 1
            print nums1
            return
        if second < 0:
            while first >= 0:
                nums1[w] = nums1[first]
                first -= 1
                w -= 1
            print nums1
            return

        if nums1[first] >= nums2[second]:
            nums1[w] = nums1[first]
            first -= 1
        else:
            nums1[w] = nums2[second]

            second -= 1

        w -= 1
    print nums1

# assert merge_two_sorted_array([1,2,3,0,0,0], 3, [2,5,6], 3) == [1,2,2,3,5,6]


merge_two_sorted_array([1,2,3,10,11, 100,100,1000, 0,0,0,0,0,0], 8, [2,5,6,7,10,123], 6)

merge_two_sorted_array([1,0,0,0,0,0,0], 1, [2,5,6,7,10,123], 6)

merge_two_sorted_array([0,0,0,0,0,0], 0, [2,5,6,7,10,123], 6)

merge_two_sorted_array([], 0, [], 0)

merge_two_sorted_array([0,0,0], 0, [1,56, 89], 3)

merge_two_sorted_array([89,0], 1, [89], 1)