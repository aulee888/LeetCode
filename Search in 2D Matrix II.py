class Solution:
    def searchMatrix(self, matrix, target):
        def row_binary(first, last):
            """Searches through the rows based on the first and last index"""
            if first > last:
                return False

            mid = first + (first - last) // 2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                return col_binary(matrix[mid], 0, len(matrix[mid]) - 1)

            elif target < matrix[mid][0]:
                return row_binary(first, mid - 1)

            elif target > matrix[mid][-1]:
                return row_binary(mid + 1, last)

        def col_binary(row, first, last):
            """Searches a given row in the matrix for target"""
            if first > last:
                return False

            mid = first + (first - last) // 2

            if row[mid] == target:
                return True

            elif target < row[mid]:
                return col_binary(row, first, mid - 1)

            elif target > row[mid]:
                return col_binary(row, mid + 1, last)

            for i in range(len(matrix)):

                for j in range(len(matrix[0])):

                    if matrix[i][j] == target:
                        return True

            return False

    def searchMatrix2(self, matrix, target):
        """Searches by iterating through each row on matrix and using binary
        search on the row.
        """
        def binary(row, first, last):
            if first > last:
                return False

            mid = first + (last - first) // 2

            if matrix[row][mid] == target:
                return True

            elif target < matrix[row][mid]:
                return binary(row, first, mid - 1)

            elif target > matrix[row][mid]:
                return binary(row, mid + 1, last)

        if matrix:
            m = len(matrix)

            if matrix[0]:
                n = len(matrix[0]) - 1

                for i in range(m):
                    if binary(i, 0, n):
                        return True

        return False
