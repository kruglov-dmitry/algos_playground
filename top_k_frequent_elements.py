#
#   https://leetcode.com/problems/top-k-frequent-elements/
#


from heapq import heapify, heappop


def top_k_frequent_elements(nums, k):

    d = {}
    for entry in nums:
        d[entry] = 1 + d.get(entry, 0)

    cnt_by_val = {}

    for key in d:
        cnt_by_val[d[key]] = cnt_by_val.get(d[key], []) + [key]

    cnts = [-x for x in d.values()]

    heapify(cnts)

    res = []
    v = set()
    while k and cnts:
        cur = -heappop(cnts)
        if cur not in v:
            res += cnt_by_val[cur]
            v.add(cur)

        k -= 1

    return res


print top_k_frequent_elements([1,2], 2)

print top_k_frequent_elements([1,2,3], 3)

print top_k_frequent_elements([1,2,3], 2)
