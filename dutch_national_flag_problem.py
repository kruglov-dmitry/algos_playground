def dnf(nums):
    """
    :input nums: list[int] where every entry in [0, 1, 2]
    :return re-order in place original array to group all entry in order
    """
    i = 0
    j = 0
    max_len = len(nums) - 1

    while j <= max_len:
        entry = nums[j]
        print entry
        if entry == 0:
            tmp = nums[i]
            nums[i] = entry
            nums[j] = tmp
            i += 1
            j += 1
        elif entry == 2:
            tmp = nums[max_len]
            nums[max_len] = entry
            nums[j] = tmp
            max_len -= 1
        else:
            j += 1
