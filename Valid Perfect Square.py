class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        def helper(first, last):
            if first > last:
                return False

            mid = (first + last) // 2
            print(mid)

            if mid ** 2 == num:
                return True

            if mid ** 2 < num:
                return helper(mid + 1, last)

            if mid ** 2 > num:
                return helper(first, mid - 1)

        if num <= 1:  # Base case; num - 1 yields first > last -> False
            return True

        return helper(1, num - 1)