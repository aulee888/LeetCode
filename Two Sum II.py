class Solution:
    def rec_twoSum(self, numbers: list, target: int) -> list:
        """Recursive binary search
        Time Complexity: O(n*log(n))
        """
        def binary_search(pos, first, last):
            mid = (first + last) // 2

            if mid == last:  # Base case
                if numbers[pos] + numbers[mid] == target:
                    return [pos + 1, mid + 1]
                else:
                    return False

            if numbers[pos] + numbers[mid] == target:
                return [pos+1, mid+1]  # Accounts for non-zero index

            elif numbers[pos] + numbers[mid] < target:
                return binary_search(pos, mid+1, last)

            elif numbers[pos] + numbers[mid] > target:
                return binary_search(pos, first, mid)

        n = len(numbers)

        for i in range(n):
            result = binary_search(i, i+1, n-1)
            if result:
                return result

    def it_twoSum(self, numbers: list, target: int) -> list:
        """Two Point solution
        Runs in half the time a recursive binary search takes on LeetCode
        Time complexity: O(n)
        """
        i = 0
        j = len(numbers) - 1
        while i <= j:
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]

            elif numbers[i] + numbers[j] < target:
                i += 1

            elif numbers[i] + numbers[j] > target:
                j -= 1
