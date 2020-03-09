class Solution:
    def combination(self, n):
        """Example of how to arrange combinations of 3 with numbers 1 -> n"""
        output = []
        temp = []

        for i in range(1, n):
            temp.append(i)

            for j in range(i + 1, n + 1):
                temp.append(j)

                for k in range(j + 1, n + 1):
                    temp.append(k)
                    output.append(temp[:])
                    temp.pop()

                temp.pop()

            temp.pop()

        return output


    def combine(self, n, k):
        """
        Creates all combos of size k using numbers 1 -> n.
        Does so by starting with lowest possible values in each slot.
        Increase last slot until last slot == k.
        Then increase slot to its left by 1 and change k back to lowest value.
        Repeat.
        Known as Depth-First Search (DFS) --- Algorithm for traversing trees
        and explores as far as possible along each branch before backtracking.
        """
        output = []

        def helper(start, curr):
            # Must be (k - 1) b/c for loop appends one more element before
            # adding to output.
            if len(curr) == k - 1:
                for i in range(start, n + 1):
                    curr.append(i)
                    output.append(curr[:])
                    curr.pop()

            else:
                for j in range(start, n + 1):
                    curr.append(j)
                    helper(j + 1, curr)
                    curr.pop()

        helper(1, [])

        return output

    def combine2(self, n, k):
        """More concise DFS."""
        output = []

        def helper(start, curr):
            if len(curr) == k:
                output.append(curr)

            else:
                for i in range(start, n + 1):
                    helper(i + 1, curr + [i])

        helper(1, [])

        return output
