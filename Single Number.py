class Solution:
    def singleNumber(self, nums: list) -> int:
        dict = {}
        for num in nums:
            try:
                dict.pop(num)
            except:
                dict[num] = 1
        return dict.popitem()[0]

print(Solution().singleNumber([4, 1, 2, 1, 2]))