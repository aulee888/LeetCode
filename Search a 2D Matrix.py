class Solution:
    def searchMatrix(self, matrix: list, target: int) -> bool:
        def binary_matrix(first, last):
            """Uses a recursive binary search on the matrix until a row
            containing the target is found. Then uses another recursive binary
            search on the row containing the target.
            """
            if first >= last:  # Base case; when the prev recursion is one list
                return False

            mid = (first + last) // 2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                return binary_list(matrix[mid], 0, len(matrix[mid]) - 1)

            if target < matrix[mid][0]:
                return binary_matrix(0, mid - 1)

            if target > matrix[mid][-1]:
                return binary_matrix(mid + 1, last)

        def binary_list(alist, first, last):
            if first > last:  # Base case; when the prev recursion is one list
                return False

            mid = (first + last) // 2

            if target == alist[mid]:  # Base case
                return True

            if target < alist[mid]:
                return binary_list(alist, first, mid - 1)

            if target > alist[mid]:
                return binary_list(alist, mid + 1, last)


        def binary_all(first, last):
            """Binary search but last = m x n (5 x 6) = 30.
            Treats the matrix as if it were 1D.
            """
            if first > last:
                return False

            mid = (first + last) // 2
            # If 3 x 5 matrix, mid = 7, index_row = 7 // 3 = 2
            # index_col = 7 % 3 = 1
            #   0  1  2
            #   3  4  5
            #   6  7  8
            #   9 10 11
            #  12 13 14
            row = mid // len(matrix[0])
            col = mid % len(matrix[0])

            if matrix[row][col] == target:
                return True

            if target < matrix[row][col]:
                return binary_all(first, mid - 1)

            if target > matrix[row][col]:
                return binary_all(mid + 1, last)

        # Binary Matrix solution
        # if not matrix or not matrix[0]:
        #     return False
        #
        # return binary_matrix(0, len(matrix) - 1)

        # Binary All solution
        # Say we have 5 x 6 matrix, there are 30 elements in this matrix.
        # But there is index 0 to account for; subtract one for indices 0-29.
        start = 0
        end = len(matrix) * len(matrix[0]) - 1

        if not matrix or not matrix[0]:
            return False

        return binary_all(start, end)
