#
#   https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
#


def find_rotated(arr, start, end, target):
    diff = end - start

    if diff < 2:
        if arr[start] == target:
            return True
        if arr[end] == target:
            return True

        return False

    mid = start + diff / 2 + diff % 2
    if arr[mid] == target:
        return True

    if arr[mid] == arr[end]:
        if find_rotated(arr, start, mid, target):
            return True
        return find_rotated(arr, mid, end, target)

    if target < arr[mid]:
        if arr[mid] <= arr[end]:
            return find_rotated(arr, start, mid, target)

        if target > arr[end]:
            return find_rotated(arr, start, mid, target)

        return find_rotated(arr, mid, end, target)

    # target > arr[mid]:
    if arr[mid] >= arr[start]:
        return find_rotated(arr, mid, end, target)

    if target < arr[start]:
        return find_rotated(arr, mid, end, target)

    # arr[mid] < arr[start]
    return find_rotated(arr, start, mid, target)


def solution(nums, target):
    if not nums:
        return False
    return find_rotated(nums, 0, len(nums) - 1, target)


assert solution([1,1,1,3,1], 3)

assert solution([5, 1, 3], 3)
assert solution([5, 1, 3], 5)

assert solution([3, 5, 1], 3)

assert solution([3, 5, 1], 1)

assert solution([1,3,5], 1)

assert solution([1,1,3], 3)

assert solution([1, 1, 3, 1], 3)

assert solution([2,5,6,0,0,1,2], 0)

assert not solution([2,5,6,0,0,1,2], 3)

assert solution([1,0,1,1,1,1,1], 0)

assert solution([3,0,1,1,1,1,1], 0)

assert solution([3,0,1,1,1,1,3], 0)

assert solution([3,0,1,1,1,1,3], 3)

assert solution([3,0,1,1,1,1,2], 0)

assert not solution([], 0)

assert solution([1,2], 2)

assert solution([2,1], 2)

assert not solution([1], 2)

assert solution([1], 1)

assert solution([2,1, 1], 2)

assert solution([2,0, 1], 0)
