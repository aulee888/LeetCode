# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
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
