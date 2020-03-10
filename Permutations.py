class Solution:
    def permute(self, nums):
        output = []

        def helper(leftover, curr):
            n = len(leftover)

            if n == 0:
                output.append(curr)

            else:
                for i in range(n):
                    res = curr[:] + [leftover[i]]
                    temp = leftover.pop(i)  # Removes element so it can't be used
                    helper(leftover, res)
                    leftover.insert(i, temp)  # Adds element back in for next perm

        helper(nums, [])

        return output
