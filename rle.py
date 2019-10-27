"""
https://leetcode.com/problems/string-compression

Given string, possible empty:
AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB

we need to implement RLE (run length encoding) which produce following result:
A4B3C2XYZD4E3F3A6B28

Notes:
    If symbol appears only once it doesn't changed
    If symbol appears more than once, it will be added number of repetitions
"""


def rle(chars):
    ll = len(chars)

    if ll < 2:
        return ll

    r_idx, w_idx = 1, 0

    while r_idx < ll:
        cnt = 1
        while r_idx < ll and chars[r_idx - 1] == chars[r_idx]:
            r_idx += 1
            cnt += 1

        chars[w_idx] = chars[r_idx - 1]
        w_idx += 1

        if cnt > 1:
            cur_cnt = str(cnt)
            for s in cur_cnt:
                chars[w_idx] = s
                w_idx += 1
        if r_idx == ll - 1:
            chars[w_idx] = chars[r_idx]
            w_idx += 1

        r_idx += 1

    return w_idx


def rle2(a):
    ll = len(a)
    if ll < 2:
        return ll

    w_idx, r_idx = 1, 1

    while r_idx < ll:
        if a[r_idx] == a[r_idx - 1]:
            cnt = 1
            while r_idx < ll and a[r_idx] == a[r_idx - 1]:
                r_idx += 1
                cnt += 1

            for b in str(cnt):
                a[w_idx] = b
                w_idx += 1
            if r_idx == w_idx and r_idx < ll:
                if a[w_idx - 1] == a[r_idx]:
                    r_idx += 1
                    w_idx += 1

        else:
            a[w_idx] = a[r_idx]
            w_idx += 1
            r_idx += 1

    return w_idx
