#
#   https://leetcode.com/problems/trim-a-binary-search-tree
#


def trim_binary_search_tree(root, start, end):
    if not root:
        return root

    if start <= root.val <= end:
        root.right = trim_binary_search_tree(root.right, start, end)
        root.left = trim_binary_search_tree(root.left, start, end)
        return root
    elif root.val < start:
        return trim_binary_search_tree(root.right, start, end)
    else:  # root.val > start:
        return trim_binary_search_tree(root.left, start, end)
