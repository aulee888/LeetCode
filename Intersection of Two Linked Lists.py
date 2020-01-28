# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """Hash table solution stores every node of list A.
        Iterate through list B until a node of A is found.
        """
        stackA = {}

        while headA:
            stackA.append(headA)
            headA = headA.next

        if not stackA:
            return None

        while headB:
            if headB in stackA:
                return headB

            headB = headB.next

        return None

    def getIntersectionNode(self, headA, headB):
        """Two pointer solution
        When headA reaches end of list, set it to
        top of headB. Set headB to top of headA when it reaches its end. The
        two will meet at intersection.
        If no intersection, at some point both will be None."""
        if not headA or not headB:
            return None

        pA = headA
        pB = headB

        while pA != pB:
            if pA:
                pA = pA.next
            else:
                pA = headB

            if pB:
                pB = pB.next
            else:
                pB = headA

        return pA