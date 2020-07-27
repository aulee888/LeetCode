class ListNode:
    """
    Used for debugging LeetCode scripts
    """
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def create(self, l1: list):
        if l1:
            head = ListNode(l1[0])
            top = head

            for item in l1[1:]:
                head.next = ListNode(item)
                head = head.next

            return top

        else:
            return []

    def __repr__(self):
        linked_list = []

        while self.next:
            linked_list.append(self.val)
            self.val = self.next.val
            self.next = self.next.next

        linked_list.append(self.val)

        return f'{linked_list}'
