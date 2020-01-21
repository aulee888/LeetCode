# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """Two pass solution"""
        # Simplify corner cases i.e only one node or removing head
        dummy = ListNode(0)
        dummy.next = head
        curr = head
        position = 0

        while curr:
            position += 1
            curr = curr.next

        position -= n
        curr = dummy

        while position > 0:
            position -= 1
            curr = curr.next

        # By modifying this, we're really changing the list b/c dummy and curr
        # point to same object.
        curr.next = curr.next.next

        return dummy.next

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """One pass solution, maintaining an (n + 1) gap b/w two pointers"""
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy

        for i in range(n + 1):
            first = first.next

        while first:
            first = first.next
            second = second.next

        second.next = second.next.next

        return dummy.next