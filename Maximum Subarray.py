class Solution:
    def maxSubArray1(self, nums: list) -> int:
        """Attempt at a divide and conquer solution"""
        def rec_helper(first, last):
            if first == last:
                return first

            mid = (first + last) // 2

            left = rec_helper(first, mid)
            right = rec_helper(mid + 1, last)

            count = 0
            for i in range((last + 1) - first):
                count += nums[left + i]

            for j in range(first, last + 1):
                if nums[first] > count:
                    pass


            if (left + right) > left and (left + right) > right:
                return left + right

            elif left > right:
                return left

            else:
                return right

    def maxSubArray(self, nums):
        n = len(nums)
        curr_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, n):
            if curr_sum < 0:
                curr_sum = nums[i]

            else:
                curr_sum += nums[i]

            if curr_sum > max_sum:
                max_sum = curr_sum

        return max_sum
