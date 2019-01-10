# coding=utf-8
import random

#
#   Implicit Treap implementation
#
#   Based on:
#       1. http://e-maxx.ru/algo/treap
#       2. https://threads-iiith.quora.com/Treaps-One-Tree-to-Rule-em-all-Part-2
#       3. https://neerc.ifmo.ru/wiki/index.php?title=%D0%94%D0%B5%D0%BA%D0%B0%D1%80%D1%82%D0%BE%D0%B2%D0%BE_%D0%B4%D0%B5%D1%80%D0%B5%D0%B2%D0%BE_%D0%BF%D0%BE_%D0%BD%D0%B5%D1%8F%D0%B2%D0%BD%D0%BE%D0%BC%D1%83_%D0%BA%D0%BB%D1%8E%D1%87%D1%83
#

random.seed()


def split(root, num_of_elements):

    if not root:
        return None, None

    left_size = 0
    if root.left:
        left_size = root.left.size

    if left_size >= num_of_elements:
        left, right = split(root.left, num_of_elements)
        root.left = right
        root.update_size()

        return left, root
    else:
        left, right = split(root.right, num_of_elements - left_size - 1)
        root.right = left
        root.update_size()

        return root, right


def merge(treap_1, treap_2):
    if not treap_2:
        return treap_1

    if not treap_1:
        return treap_2
    elif treap_1.priority > treap_2.priority:
        treap_1.right = merge(treap_1.right, treap_2)
        treap_1.update_size()
        return treap_1
    else:
        treap_2.left = merge(treap_1, treap_2.left)
        treap_2.update_size()
        return treap_2


def get_min_impl(node):
    if node.left:
        return get_min_impl(node.left)

    return node.value


def get_max_impl(node):
    if node.right:
        return get_max_impl(node.right)

    return node.value


def print_in_order(root):

    if root:
        print_in_order(root.left)
        print root.value,
        print_in_order(root.right)


def level_order(root):

    depth = 0
    queue = [(root, depth)]

    while queue:
        cur, cur_depth = queue.pop(0)
        if cur:
            print "Depth ", cur_depth, "Value", cur.value, "Size: ", cur.size
            queue.append((cur.left, cur_depth+1))
            queue.append((cur.right, cur_depth+1))


class Node(object):
    __slots__ = ['value', 'priority', 'size', 'left', 'right']

    def __init__(self, value):
        self.value = value
        self.priority = random.random()

        self.size = 1
        self.left = None
        self.right = None

    def update_size(self):
        ls = 0
        if self.left:
            ls = self.left.size

        rs = 0
        if self.right:
            rs = self.right.size

        self.size = ls + rs + 1

    def show(self):
        print_in_order(self)


class ImplicitTreap(object):
    __slots__ = ['root']

    def __init__(self):
        self.root = None

    def insert(self, new_val):

        new_subtree = Node(new_val)
        self.root = merge(self.root, new_subtree)

    def exec_command_1(self, start_idx, end_idx):

        left_1, right_1 = split(self.root, end_idx)         # A[0:end_idx], A[end_idx:]
        left_2, right_2 = split(left_1, start_idx-1)        # A[0:start_idx], A[start_idx, end_idx]

        first_part = merge(right_2, left_2)

        self.root = merge(first_part, right_1)

    def exec_command_2(self, start_idx, end_idx):
        left_1, right_1 = split(self.root, end_idx)         # A[0:end_idx], A[end_idx:]
        left_2, right_2 = split(left_1, start_idx - 1)      # A[0:start_idx], A[start_idx, end_idx]

        first_part = merge(left_2, right_1)
        self.root = merge(first_part, right_2)

    def show(self):
        print_in_order(self.root)

    def get_min(self):
        return get_min_impl(self.root)

    def get_max(self):
        return get_max_impl(self.root)
