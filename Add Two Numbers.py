# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num_string1, num_string2 = '', ''
        l3 = None

        while l1 is not None:
            num_string1 = str(l1.val) + num_string1
            l1 = l1.next

        while l2 is not None:
            num_string2 = str(l2.val) + num_string2
            l2 = l2.next

        num_string3 = int(num_string1) + int(num_string2)
        num_string3 = str(num_string3)

        for i in range(len(num_string3)):
            temp = ListNode(int(num_string3[i]))
            temp.next = l3
            l3 = temp

        return l3
