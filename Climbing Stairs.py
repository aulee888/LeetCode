class Solution:
    """Recursive Solution"""
    def recClimbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        else:
            step1 = self.recClimbStairs(n - 1)
            step2 = self.recClimbStairs(n - 2)

            return step1 + step2

    def dpClimbStairs(self, n: int, known: dict) -> int:
        """Dynamic Programming Solution w/ Recursion"""

        if n in known:
            return known[n]

        if n <= 2:
            return n

        ways = (self.dpClimbStairs(n - 1, known)
                + self.dpClimbStairs(n - 2, known))
        known[n] = ways

        return ways