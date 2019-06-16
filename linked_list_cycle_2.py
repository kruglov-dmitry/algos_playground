#
#   https://leetcode.com/problems/linked-list-cycle-ii/
#
#   Given linked list find a node where cycle started
#
#   Classical Floyd approach: https://en.wikipedia.org/wiki/Cycle_detection#Floyd's_Tortoise_and_Hare
#


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def solution(head):
    cycle_present = False

    fast = slow = head

    while fast and slow:
        slow = slow.next
        if fast.next:
            fast = fast.next.next
        else:
            return None

        if fast == slow:
            cycle_present = True
            break

    if not cycle_present:
        return None

    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow


# input = [3,2,0,-4]
# root = ListNode(3)
# n1 = ListNode(2)
# n2 = ListNode(0)
# n3 = ListNode(-4)
# root.next = n1
# n1.next = n2
# n2.next = n3
# n3.next = n1
#
# print solution(root).val

root = ListNode(1)
w = ListNode(2)
root.next = w
w.next = root
print solution(root).val
