#
#   https://leetcode.com/problems/container-with-most-water/
#


def container_with_most_water(heights):
    lo, hi = 0, len(heights) - 1

    all_max = lo * hi

    while lo < hi:
        if heights[lo] < heights[hi]:
            lo += 1
        else:
            hi -= 1

        cur_max = (hi - lo) * min(heights[lo], heights[hi])
        if cur_max > all_max:
            all_max = cur_max

    return all_max


assert container_with_most_water([1,8,6,2,5,4,8,3,7]) == 49

assert container_with_most_water([1,8,6]) == 6

assert container_with_most_water([100,90,10]) == 90

assert container_with_most_water([1,8]) == 1

assert container_with_most_water([4, 8, 10, 15, 8, 10]) == 32

assert container_with_most_water([1, 3, 2, 5, 25, 24, 5]) == 24

assert container_with_most_water([5, 24, 25, 5, 2, 3, 1]) == 24
