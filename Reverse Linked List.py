class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        """Iterative solution"""
        new_head = None

        while head:
            curr = ListNode(head.val)
            curr.next, new_head = new_head, curr

            head = head.next

        return new_head

    def reverseList2(self, head):
        """Recursive solution"""
        if not head or not head.next:
            return head

        new = Solution().reverseList2(head.next)
        head.next.next = head
        head.next = None

        return new