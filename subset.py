#
#   https://leetcode.com/problems/subsets/
#


def subset(nums):
    res = [[]]

    for r in nums:
        res += [x + [r] for x in res]

    return res


def subset_ii(nums):
    res = [[]]

    q = [[x] for x in nums]

    cache = set()

    while q:
        cur = q.pop()
        res.append(cur)
        for num in nums:
            if num not in cur:
                new = sorted(cur+[num])
                new_cache = str(new)
                if new_cache not in cache:
                    q.append(new)
                    cache.add(new_cache)

    return res
