# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        Utilizes two pointers:
        1. Dummy for tracking nodes in answer
        2. Curr for checking for duplicates as you traverse head
        """
        dummy = ListNode(0)
        dummy.next = head
        top = dummy

        if not head:  # Corner case; if head is empty
            return None

        curr = head.next

        while curr:
        # Two while loops to skip over sequential duplicate elements
        # i.e [1, 2, 2, 3, 3, 4] to return  [1 ,4]
            while curr and head.val == curr.val:

                while curr and head.val == curr.val:
                    curr = curr.next

                head = curr
                if curr:  # For when curr is at end of list
                    curr = curr.next

            dummy.next = head
            dummy = dummy.next
            head = curr

            if curr:  # For when curr is at end of list
                curr = curr.next

        return top.next
