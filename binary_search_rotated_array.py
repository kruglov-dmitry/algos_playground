#
#   Given sorted array as circular buffer or just rotated sorted array
#   Implement binary search
#
#   Input: [7, 3, 1, 2], 1
#   OUTPUT: 2
#
#   Input: [7, 3, 1, 2], 10
#   OUTPUT: -1
#

def find_rotated(arr, start, end, elem):
    if start > end:
        return -1
    mid = start + (end - start) / 2
    if arr[mid] == elem:
        return mid

    if start == mid:
        if arr[end] == elem:
            return end
        else:
            return -1
    elif arr[start] < arr[mid]:
        if arr[start] <= elem < arr[mid]:
            return find_rotated(arr, start, mid - 1, elem)
        else:
            return find_rotated(arr, mid + 1, end, elem)
    else:
        if arr[mid] < elem <= arr[end]:
            return find_rotated(arr, mid + 1, end, elem)
        else:
            return find_rotated(arr, start, mid - 1, elem)


solution = find_rotated


def test_simple():
    test = [7, 8, 1, 2, 3, 4, 5, 6]
    for x in xrange(1, 9):
        assert solution(test, 0, len(test)-1, x) == (x + 1) % 8


def test_advanced():
    test = [7, 8, 9, 10, 11, 12, 1, 2, 3, 4, 5, 6]
    for x in xrange(1, 13):
        assert solution(test, 0, len(test)-1, x) == (x + 5) % 12

    assert solution(test, 0, len(test)-1, -1) == -1
    assert solution(test, 0, len(test)-1, 100) == -1


def test_small():
    test = [100, 1]
    assert solution(test, 0, len(test)-1, 1) == 1
    assert solution(test, 0, len(test)-1, 100) == 0
    assert solution(test, 0, len(test)-1, -102) == -1
    assert solution(test, 0, len(test)-1, 102) == -1
    assert solution(test, 0, len(test)-1, 13) == -1


def test_last():
    test = [100500, 13, 34, 48]
    assert solution(test, 0, len(test)-1, 1) == -1
    assert solution(test, 0, len(test)-1, 13) == 1
    assert solution(test, 0, len(test)-1, 1000) == -1
    assert solution(test, 0, len(test)-1, 30) == -1
    assert solution(test, 0, len(test)-1, 50) == -1
    assert solution(test, 0, len(test)-1, 0) == -1


test_simple()
test_advanced()
test_small()
test_last()

#
#   Initial approach - seems to be working as well, but 5 times more code >_<
#


DEBUG = False
cnt = 0

def binary_search(arr, mid, sz, elem, last_idx, searched_in_other_part):
    global cnt

    if mid < 0:
        raise

    if mid == last_idx:
        return -1

    if arr[mid - 1] == elem:
        return mid - 1

    if arr[last_idx - 1] == elem:
        return last_idx - 1

    if mid > last_idx:
        tmp = last_idx
        last_idx = mid
        mid = tmp

    if DEBUG:
        print mid, arr[mid-1], last_idx, arr[last_idx - 1]

    #
    #       Searching in left sub-array
    #
    if elem < arr[mid - 1] < arr[last_idx - 1]:
        if DEBUG:
            print("LEFT 1 - ORDINAL ORDERING")
        new_mid = mid - abs(last_idx - mid) // 2 - abs(last_idx - mid) % 2
        return binary_search(arr, new_mid, sz, elem, mid, searched_in_other_part)
    elif arr[mid - 1] > elem > arr[last_idx - 1] and last_idx == sz:
        if DEBUG:
            print("LEFT 2 - ORDINAL ORDERING - MOVE TOWARDS CIRCULAR START")
        new_mid = mid // 2 + mid % 2
        return binary_search(arr, new_mid, sz, elem, mid, searched_in_other_part)
    elif arr[mid - 1] > elem > arr[last_idx - 1] and arr[mid - 1] > arr[last_idx - 1] and last_idx != sz and searched_in_other_part:    # [7, 8, 1, 2, ... , ]
        if DEBUG:
            print("LEFT 3 - FROM CIRCULAR START")
        new_mid = mid // 2 + mid % 2
        return binary_search(arr, new_mid, sz, elem, mid, searched_in_other_part)
    #
    #       Searching in right sub-array
    #
    elif elem > arr[mid - 1] > arr[last_idx - 1] and not searched_in_other_part:
        if DEBUG:
            print("RIGHT 1 - ORDINAL ORDERING")
        if mid + 1 == last_idx:
            return -1
        new_mid = mid + abs(last_idx - mid) // 2 + abs(last_idx - mid) % 2
        if new_mid < mid:
            raise
        return binary_search(arr, new_mid, sz, elem, mid, searched_in_other_part)
    elif arr[mid - 1] > elem > arr[last_idx - 1] and arr[mid - 1] > arr[last_idx - 1] and last_idx != sz and not searched_in_other_part:    # [7, 8, 1, 2, ... , ]
        if DEBUG:
            print("RIGHT 2 - FROM CIRCULAR START")
        new_mid = last_idx + (sz - last_idx) // 2 + (sz - last_idx) % 2
        if new_mid < mid:
            raise
        return binary_search(arr, new_mid, sz, elem, last_idx, searched_in_other_part)
    elif arr[mid - 1] < elem < arr[last_idx - 1]:
        if DEBUG:
            print("RIGHT 3 - ORDINAL ORDERING - BETWEEN LAST AND CURRENT")
        if mid + 1 == last_idx:
            return -1
        new_mid = mid + abs(last_idx - mid) // 2 + abs(last_idx - mid) % 2
        return binary_search(arr, new_mid, sz, elem, mid, searched_in_other_part)
    elif elem > arr[mid - 1] and elem > arr[last_idx - 1] > arr[mid - 1] and last_idx < sz:
        if DEBUG:
            print("RIGHT 4 - MORE THAN PREV AND CURRENT - START SEARCH IN RIGHT PART")

        new_mid = last_idx + (sz - last_idx) // 2 + (sz - last_idx) % 2
        return binary_search(arr, new_mid, sz, elem, last_idx, searched_in_other_part)
    elif sz == last_idx and elem > arr[mid - 1] and elem > arr[last_idx - 1] > arr[mid - 1]:
        if DEBUG:
            print("RIGHT 5 - MORE THAN PREV AND CURRENT - START SEARCH IN LEFT PART")
        mid = sz // 2 + sz % 2
        new_mid = mid // 2 + mid % 2
        searched_in_other_part = True
        return binary_search(arr, new_mid, sz, elem, mid, searched_in_other_part)
    elif arr[mid - 1] > elem and elem < arr[last_idx - 1]:
        if DEBUG:
            print("RIGHT 6 - ORDINAL ORDERING - BETWEEN LAST AND CURRENT")
        if mid + 1 == last_idx:
            return -1
        new_mid = mid + abs(last_idx - mid) // 2 + abs(last_idx - mid) % 2
        return binary_search(arr, new_mid, sz, elem, mid, searched_in_other_part)
    else:
        print mid,
        raise

def not_so_elegant_solution(arr, elem):
    sz = len(arr)

    if sz < 1:
        return -1

    if sz == 1:
        if arr[0] == elem:
            return 0
        else:
            return -1

    mid = sz // 2 + sz % 2
    searched_in_left_part = False
    return binary_search(arr, mid, sz, elem, sz, searched_in_left_part)