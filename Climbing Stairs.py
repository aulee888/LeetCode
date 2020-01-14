class Solution:
    def rec_climbStairs(self, n: int) -> int:
        """Recursive Solution"""
        if n <= 2:
            return n

        else:
            step1 = self.rec_climbStairs(n - 1)
            step2 = self.rec_climbStairs(n - 2)

            return step1 + step2

    def dp_climbStairs(self, n: int) -> int:
        """Dynamic Programming Solution w/ Recursion"""
        def helper(steps: int, known: dict) -> int:
            if steps in known:
                return known[steps]

            if steps <= 2:
                return steps

            ways = (helper(steps - 1, known)
                    + helper(steps - 2, known))
            known[steps] = ways

            return ways

        return helper(n, {})
