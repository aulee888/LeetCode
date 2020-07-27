from ListNode import ListNode


class Solution:
    def swapPairs(self, head):
        if head and head.next:
            top = head.next

        else:
            return head

        front = None
        curr = head

        while curr and curr.next:
            print(f'Current: {curr.val}')
            back = curr.next.next

            first = curr
            second = curr.next

            # Swaps the adjacent nodes
            print(f'Swapping {first.val} <--> {second.val}')
            second.next = first
            first.next = back
            curr = second

            # Adds front of list before the swapped nodes
            if front:  # Corner case; Beginning of list
                print(f'Connecting front {front.val} -> {curr.val}')
                front.next = curr

            # Adds the back of the list after the swapped nodes
            print(f'Appending back of list: {curr.val} -> {curr.next.val} -> /'
                  f'{back.val if back else None}')
            curr.next.next = back

            # Designates a new front of list
            front = first

            # Move focus to after the swapped nodes
            curr = curr.next.next

            print('')

        return top
