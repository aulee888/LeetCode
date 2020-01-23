class Solution:
    def maxSubArray(self, nums):
        n = len(nums)
        curr_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, n):
            # Even if all nums were < 0, adding negatives makes a more
            # negative number
            if curr_sum < 0:
                curr_sum = nums[i]

            else:
                curr_sum += nums[i]

            if curr_sum > max_sum:
                max_sum = curr_sum

        return max_sum
