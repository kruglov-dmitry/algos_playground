class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()
        ll = len(nums)

        res = []

        for idx in xrange(ll - 2):
            if idx == 0 or nums[idx] > nums[idx - 1]:
                start = idx + 1
                end = ll - 1

                neg = -nums[idx]

                while start < end:
                    cur_sum = nums[start] + nums[end]
                    if cur_sum == neg:
                        cur = [nums[idx], nums[start], nums[end]]
                        res.append(cur)

                        start += 1
                        end -= 1

                        while start < end and nums[end] == nums[end + 1]:
                            end -= 1

                        while start < end and nums[start] == nums[start - 1]:
                            start += 1

                    elif cur_sum < neg:
                        start += 1
                    else:
                        end -= 1

        return res


input = [-2,0,1,1,2]        # [[-2,0,2],[-2,1,1]]

print Solution().threeSum(input)