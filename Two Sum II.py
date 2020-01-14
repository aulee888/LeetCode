class Solution:
    def twoSum(self, numbers: list, target: int) -> list:
        """Implements a recursive binary search"""
        def binary_search(pos, first, last):
            mid = (first + last) // 2
            print('First: {}, Mid: {}, Last: {}, Value: {}'.format(first, mid, last, numbers[mid]))

            #if first == last:
            #    return False

            if numbers[pos] + numbers[mid] == target:
                return [pos+1, mid+1]  # Accounts for non-zero index

            elif numbers[pos] + numbers[mid] < target:
                return binary_search(pos, mid+1, last)

            elif numbers[pos] + numbers[mid] > target:
                return binary_search(pos, first, mid)

        n = len(numbers)

        for i in range(n):
            print(i)
            print('---')
            result = binary_search(i, i+1, n-1)
            print('')
            if result:
                return result


l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print(Solution().twoSum(l1, 27))