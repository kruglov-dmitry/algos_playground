#
#   https://leetcode.com/problems/partition-labels/
#
#   Given a string - partition it to group all similar letters in one partition.
#   Maximize number of partitions.
#


def partition_labels(s):

    dct = {}
    for idx, letter in enumerate(s):
        dct[letter] = idx

    partitions = []

    idx = 0
    end = len(s)
    while idx < end:
        last = dct[s[idx]]
        cur_partition = s[idx:last+1]

        while True:
            enough = True
            for l in cur_partition:
                if dct[l] > last:
                    last = dct[l]
                    cur_partition = s[idx:last+1]
                    enough = False
                    break
            if enough:
                break

        idx = last + 1
        partitions.append(len(cur_partition))

    return partitions


S = "ababcbacadefegdehijhklij"  #     Output: [9, 7, 8]

print partition_labels(S)