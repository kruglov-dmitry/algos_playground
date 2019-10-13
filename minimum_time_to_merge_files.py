import heapq

#
#   https://leetcode.com/problems/minimum-cost-to-connect-sticks
#


def minimum_time_to_merge_files(num_of_sub_files, files):

    heapq.heapify(files)

    min_sum = 0
    while len(files) > 1:
        cur_sum = heapq.heappop(files) + heapq.heappop(files)
        min_sum += cur_sum
        heapq.heappush(files, cur_sum)

    return min_sum


numOfSubFiles = 4
files = [20, 4, 8, 2]

numOfSubFiles = 6
files = [1, 2, 5, 10, 35, 89]

# [1, 2, 5, 10, 35, 89] 0
# [1, 3, 5, 10, 35, 89] 3
# [1, 3, 8, 10, 35, 89] 8
# [1, 3, 8, 18, 35, 89] 18
# [1, 3, 8, 18, 53, 89] 53
# [1, 3, 8, 18, 53, 142] 142

print minimum_time_to_merge_files(numOfSubFiles, files)