class Solution:
    def mySqrt(self, x: int) -> int:

        def binary_search(alist, first, last):
            """Only works for values greater than 2 due to list creation"""
            mid = (first + last) // 2

            if alist[mid] ** 2 == x:
                return alist[mid]

            elif alist[mid] ** 2 > x:
                if alist[mid - 1] ** 2 < x:
                    return alist[mid - 1]
                else:
                    return binary_search(alist, first, mid)

            elif alist[mid] ** 2 < x:
                if alist[mid + 1] ** 2 > x:
                    return alist[mid]
                else:
                    return binary_search(alist, first + 1, last)

        if x == 0:
            return 0

        elif x in [1, 2]:
            return 1

        else:
            alist = [i for i in range(0, x)]
            return binary_search(alist, 0, x)

print(Solution().mySqrt(2147395599))
print(Solution().mySqrt(100))
