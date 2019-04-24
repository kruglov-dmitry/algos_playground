#
#   https://leetcode.com/problems/binary-search/
#


def bin_search(arr, elem, l, r):

    if l == r:
        if elem == arr[l]:
            return l
        else:
            return -1

    if r - l == 1:
        if arr[l] == elem:
            return l
        if arr[r] == elem:
            return r
        return -1

    mid = l + (r - l) // 2 + (r - l) % 2

    if arr[mid] > elem:
        return bin_search(arr, elem, l, mid)
    else:
        return bin_search(arr, elem, mid, r)


def binary_search(arr, elem):
    sz = len(arr)
    return bin_search(arr, elem, 0, sz-1)


def run_tests():
    test = [1, 2, 3, 4, 5, 6, 7, 8]
    assert binary_search(test, 6) == 5
    assert binary_search(test, 7) == 6
    assert binary_search(test, 3) == 2
    assert binary_search(test, 2) == 1
    assert binary_search(test, -12) == -1
    assert binary_search(test, 12) == -1

    assert binary_search([5], 5) == 0
    assert binary_search([5], 15) == -1

    test = [-1, 0, 3, 5, 9, 12]
    assert binary_search(test, -1) == 0
    assert binary_search(test, 8) == -1
    assert binary_search(test, 5) == 3

run_tests()