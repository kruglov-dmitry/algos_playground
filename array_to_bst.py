#
#   https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
#


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def array_to_binary_search_tree(arr):
    if not arr:
        return None

    mid = len(arr) // 2
    root = TreeNode(arr[mid])
    root.left = array_to_binary_search_tree(arr[:mid])
    root.right = array_to_binary_search_tree(arr[mid+1:])

    return root


def print_tree(root):
    if not root:
        return

    print(root.val)
    print_tree(root.left)
    print_tree(root.right)


arr1 = [-10,-3,0,5,9]

arr2 = [1,2,3]

print_tree(array_to_binary_search_tree(arr2))