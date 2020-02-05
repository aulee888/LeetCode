class Solution:
    def findMin(self, nums: list) -> int:
        def divCon(first, last):
            if first == last:  # Base case; when one element
                return nums[first]

            mid = (first + last) // 2
            left_min = divCon(first, mid)
            right_min = divCon(mid + 1, last)

            if left_min <= right_min:
                return left_min
            else:
                return right_min

        return divCon(0, len(nums) - 1)
