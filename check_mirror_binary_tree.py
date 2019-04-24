#
#   https://leetcode.com/problems/symmetric-tree/
#
#
#   Given a root of binary tree - check whether it is symmetric related to root
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#
#   Optimized version:
#

def is_mirror(left, right):
    if not left or not right:
        return left == right
    if left.val != right.val:
        return False
    return is_mirror(left.left, right.right) and is_mirror(left.right, right.left)


def is_symmetric_v2(root):
    return is_mirror(root, root)

#
#   Initial, not so optimal version
#


def is_symmetric_v1(root):

    def unroll(root, level, cur_array):
        if root:
            cur_array[level].append(root.val)
            unroll(root.left, level + 1, cur_array)
            unroll(root.right, level + 1, cur_array)
        else:
            cur_array[level].append(None)

    if not root:
        return True

    from collections import defaultdict
    left = defaultdict(list)
    right = defaultdict(list)
    level = 2
    unroll(root.left, level, left)
    unroll(root.right, level, right)

    l1 = len(left)
    l2 = len(right)
    if l1 != l2:
        return False

    for level in left:
        n1 = len(left[level])
        n2 = len(right[level])
        if n1 != n2:
            return False

        for idx in xrange(n1):
            if left[level][idx] != right[level][n2 - idx - 1]:
                return False

    return True
