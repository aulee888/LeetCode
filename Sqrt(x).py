class Solution:
    def mySqrt(self, x: int) -> int:

        def binary_search(first, last):
            """Only works for values greater than 2 due to list creation.
            Avoids using a list which uses too much memory for large numbers.
            """
            mid = (first + last) // 2

            if mid ** 2 == x:
                return mid

            elif mid ** 2 > x:
                if (mid - 1) ** 2 < x:
                    return mid - 1
                else:
                    return binary_search(first, mid)

            elif mid ** 2 < x:
                if (mid + 1) ** 2 > x:
                    return mid
                else:
                    return binary_search(mid + 1, last)

        if x == 0:
            return 0

        elif x in [1, 2]:
            return 1

        else:
            return binary_search(0, x)
