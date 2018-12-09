def longest_substring_fast(some_str):
    """
    :param some_str: string for analysis
    :return: longest substring found
    """

    cache = {}

    start_idx = 0

    cur_max = ""

    for idx, letter in enumerate(some_str):
        if letter in cache and start_idx <= cache[letter]:
            if len(cur_max) < idx - start_idx:
                cur_max = some_str[start_idx:idx]
            start_idx = cache[letter] + 1

        cache[letter] = idx

    if len(cur_max) < len(some_str) - start_idx:
        cur_max = some_str[start_idx:]

    return cur_max
