#
#   https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
#


def flatten_binary_tree_to_linked_list(root):
    if not root:
        return root

    new_right = flatten_binary_tree_to_linked_list(root.left)
    remaining_right = flatten_binary_tree_to_linked_list(root.right)

    root.right = new_right
    root.left = None

    if root.right:
        cur = root.right
        prev = root
        while cur:
            prev = cur
            cur = cur.right
        prev.right = remaining_right
    else:
        root.right = remaining_right

    return root

def print_tree(root):
    if not root:
        return
    print root.val
    print_tree(root.left)
    print_tree(root.right)


def print_right_only(root):
    if not root:
        return

    while root:
        print root.val
        root = root.right


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

#    1
#   / \
#  2   5
# / \   \
#3   4   6


root = Node(1)
a = Node(2)
b = Node(5)
root.left = a
root.right = b
c = Node(3)
d = Node(4)
a.left = c
a.right = d
e = Node(6)
b.right = e

# flatten_binary_tree_to_linked_list(root)
# print_right_only(root)

root = Node(5)
a = Node(6)
root.right = a
flatten_binary_tree_to_linked_list(root)
print_right_only(root)
