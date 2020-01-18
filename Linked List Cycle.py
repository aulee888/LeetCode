# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        seen = []

        if not head:  # Accounts for lists on size 1
            return False

        while head and head.next:  # Must be while head because while head.val returns wrong output on 0
            if (head.val, head.next.val) in seen:
                return True
            else:
                seen.append((head.val, head.next.val))

            head = head.next

        return False
