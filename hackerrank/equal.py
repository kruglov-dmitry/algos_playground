def equal(arr):
    """
    :param arr: list[int] of initial chocolate distribution
    :return: minimum number of rounds of rounds of chocolate distribution
    details at https://www.hackerrank.com/challenges/equal/problem
    """
    min_val = min(arr)

    min_res = 10005000

    #
    # We are going to compute min number of operations whether we can reach
    # min_val, min_val - 1, min_val - 2, min_val - 3, min_val - 4
    #

    stop_num = min_val - 4

    while min_val >= stop_num:

        cur_res = 0
        for entry in arr:
            delta = entry - min_val

            cur_res += delta / 5
            cur_res += (delta % 5) / 2
            cur_res += (delta % 5) % 2

        if min_res > cur_res:
            min_res = cur_res

        min_val -= 1

    return min_res
