# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """Hash table solution.
        Appends head instead of head.val because head records different
        objects. It is a solution to storing the same value to seen and
        having the same value show up in a different object.
        Time Complexity: O(n), Space Complexity: O(n)
        """
        seen = []

        while head:
            if head in seen:
                return True
            else:
                seen.append(head)  # Append head instead of head.val

            head = head.next

        return False

    def hasCycle(self, head: ListNode) -> bool:
        """Two pointer solution
        Pointers cannot be moving down lists at same speed otherwise they
        would never equal each other in a cycle.
        (i.e pointer2 will always be 1 ahead)
        Time Complexity: O(n), Space Complexity: O(1)
        """
        if not head:
            return False

        pointer1 = head
        pointer2 = head.next

        while pointer1 != pointer2:
            if not pointer2 or not pointer2.next:  # If pointer2 end of list
                return False

            pointer1 = pointer1.next
            pointer2 = pointer2.next.next

        return True

