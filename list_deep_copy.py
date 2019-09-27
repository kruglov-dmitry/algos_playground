#
#   https://leetcode.com/problems/copy-list-with-random-pointer
#

class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


def solution(head):
    if not head:
        return head

    mapping = {None: None}
    new_mapping = {None: None}

    root = head

    while root:
        mapping[root.val] = root.random.val if root.random else None

        new_mapping[root.val] = Node(root.val, None, None)

        root = root.next

    root = head

    while root:
        cur_node = new_mapping[root.val]

        if root.next:
            cur_node.next = new_mapping[root.next.val]

        cur_node.random = new_mapping[mapping[root.val]]

        root = root.next

    return new_mapping[head.val]
