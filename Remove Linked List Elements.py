# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while head:
            # Corner case; if there's only one element in linked list
            # Skips consecutive elements
            while head and head.val == val:
                head = head.next

            # Move prev pointer to non targeted val
            prev.next = head
            prev = prev.next

            # Keep moving head pointer until end of list
            if head:
                head = head.next

        return dummy.next
