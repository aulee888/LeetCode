# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
     ''' Iterative Solution '''
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        sorties = []
        
        while (l1 or l2):
            if l1 and l2:
                
                if l1.val < l2.val:
                    sorties.append(l1.val)
                    l1 = l1.next
                    
                else:
                    sorties.append(l2.val)
                    l2 = l2.next
                    
            elif l1 and not l2:
                sorties.append(l1.val)
                l1 = l1.next
                
            else:
                sorties.append(l2.val)
                l2 = l2.next
            
        merged = None
            
        while sorties:
            curr = ListNode(sorties.pop())
            curr.next = merged
            merged = curr
            
        return merged


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
     ''' Recursive Solution '''
    if not l1:
        return l2

    if not l2:
        return l1

    dummy = ListNode(None)

    if l1.val < l2.val:    
        dummy.next = l1
        nexthead = mergeTwoLists(l1.next, l2)
        dummy.next.next = nexthead

    else:
        dummy.next = l2
        nexthead = mergeTwoLists(l1, l2.next)
        dummy.next.next = nexthead

    return dummy.next
