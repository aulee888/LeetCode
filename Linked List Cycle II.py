#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        """Hash table solution"""
        seen = []

        while head:
            if head in seen:
                return head
            else:
                seen.append(head)

            head = head.next

        return None


    def detectCycle(self, head: ListNode) -> ListNode:
        """Two Pointer Solution"""
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break

        if not fast or not fast.next:
            return None

        if slow == fast:
            p1 = head
            p2 = fast

            while p1 != p2:
                p1 = p1.next
                p2 = p2.next

            return p1
