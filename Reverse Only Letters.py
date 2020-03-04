class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        """Time: O(n) | Space: O(n)"""
        letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        n = len(S)
        output = ''

        stack = []
        queue = []
        for j in range(n):
            if S[j] in letters:
                stack.append(S[j])
            else:
                queue.append((j, S[j]))

        for i in range(n):
            if queue and i == queue[0][0]:
                output = output + queue[0][1]
                queue.pop(0)
            else:
                output = output + stack.pop()

        return output



