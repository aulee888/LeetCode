# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        top = ListNode(0)
        top.next = head

        while head:
            # curr pointer moves along list until a non-duplicate is found
            curr = head

            while curr and head and curr.val == head.val:
                # Ensures curr and head are not None; None has no val attribute
                curr = curr.next

            head.next = curr
            head = head.next

        return top.next