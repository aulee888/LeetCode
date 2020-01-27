class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        """Bruce force solution"""
        n = len(nums)
        
        for i in range(n):

            for j in range(i + 1, n):

                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum_hash(self, nums: list, target: int) -> list:
        """One pass hash table solution"""
        n = len(nums)
        dict = {}

        for i in range(n):
            complement = target - nums[i]

            if complement in dict:
                return [dict[complement], i]

            else:
                dict[nums[i]] = i

        return 'No Solution'