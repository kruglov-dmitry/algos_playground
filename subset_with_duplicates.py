#
#   https://leetcode.com/problems/subsets-ii/
#


def subset_with_duplicates_ii(nums):
    res = [[]]
    nums.sort()
    ll = len(nums)
    idx = 0
    while idx < ll:
        count = 0
        while count + idx < ll and nums[idx] == nums[idx + count]:
            count += 1

        cur_len = len(res)
        for cc in xrange(1, count+1):
            res += [x + [nums[idx]] * cc for x in res[:cur_len]]

        idx += count

    return res


def subset_with_duplicates(nums):
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


# inp1 = [1, 2, 2]

#inp2 = [1,2,3,4,5,6,7,8,9,10]

inp3 = [4,4,4,1,4]

print subset_with_duplicates_ii(inp3)
