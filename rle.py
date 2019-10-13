"""
Given string, possible empty:
AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB

we need to implement RLE (run length encoding) which produce following result:
A4B3C2XYZD4E3F3A6B28

Notes:
    If symbol appears only once it doesn't changed
    If symbol appears more than once, it will be added number of repetitions
"""


def rle(a):
    w_idx, r_idx = 1, 1

    # [A, B, C]
    # AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB

    # [G, A, A, A, B, B, C]
    #  0  1  2  3  4  5  6
    # GA3B2C
    # 012345
    # iterations

    # w_idx 1
    # w_idx 3
    # w_idx 5

    while r_idx < len(a):
        cnt = 0
        if a[r_idx] == a[r_idx - 1]:
            while r_idx < len(a) and a[r_idx] == a[r_idx - 1]:
                r_idx += 1
                cnt += 1

            if cnt > 0:
                new_symbols = str(cnt + 1)
                for b in new_symbols:
                    a[w_idx] = b
                    w_idx += 1
        else:
            r_idx += 1

        w_idx += 1

    return a[:w_idx]
