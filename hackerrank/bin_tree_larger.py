class Node:
    def __init__(self, val):
        self.val = val
        self.left = -1
        self.right = -1


def build_tree(arr):
    idx = 0
    root = Node(arr[idx])
    head = root

    stack = [root]

    while idx < len(arr) and stack:
        cur_node = stack.pop(0)

        if idx+1 >= len(arr):
            break
        cur_l = -1
        if arr[idx+1] != -1:
            cur_l = Node(arr[idx+1])
            stack.append(cur_l)
        cur_r = -1
        if idx+2 < len(arr) and arr[idx + 2] != -1:
            cur_r = Node(arr[idx + 2])
            stack.append(cur_r)

        cur_node.left = cur_l
        cur_node.right = cur_r
        idx += 2

    return head


def helper(some_node):
    if some_node == -1:
        return 0

    return some_node.val + helper(some_node.left) + helper(some_node.right)


def bin_tree_larger(arr):
    if not arr:
        return ""

    root = build_tree(arr)
    l_sum = helper(root.left)
    r_sum = helper(root.right)
    if l_sum>r_sum:
        return "Left"

    if r_sum > l_sum:
        return "Right"

    return ""


arr = [3,6,2,9,-1,10]
assert "Left" == bin_tree_larger(arr)

arr = [3,6,2]
assert "Left" == bin_tree_larger(arr)

arr = [3,-1,2]
assert "Right" == bin_tree_larger(arr)
