class Solution:
    def generate(self, numRows: int) -> list:
        """Naive recursive solution"""
        def helper(curr):
            if curr == numRows:
                return

            if curr == 0:
                ans.append([1])
                helper(curr + 1, ans[-1])

            if curr == 1:
                ans.append([1, 1])
                helper(curr + 1, ans[-1])

            if curr >= 2 :
                n = len(ans[-1])
                to_add = [1]

                for i in range(n):
                    if i == n - 1:
                        break

                    to_add.append(ans[-1][i] + ans[-1][i + 1])

                to_add.append(1)

                ans.append(to_add)
                helper(curr + 1, ans[-1])

        ans = []
        helper(0, [])

        return ans

    def dpGenerate(self, numRows: int) -> list:
        """Dynamic Programming Solution"""
        triangle = []

        for row in range(numRows):
            to_add = [None for i in range(row + 1)]
            to_add[0], to_add[-1] = 1, 1

            for j in range(1, len(to_add) - 1):
                to_add[j] = triangle[-1][j - 1] + triangle[-1][j]

            triangle.append(to_add)

        return triangle
