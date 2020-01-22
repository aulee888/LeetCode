class Solution:
    def majorityElement(self, nums: list) -> int:
        def divCon(first, last):
            """Each of the returns will return the majority element"""
            # Base case; majority element of size 1 array is itself
            if first == last:
                return nums[first]

            mid = (first + last) // 2
            left = divCon(first, mid)
            right = divCon(mid + 1, last)

            # If two halves agree on same element, return it
            if left == right:
                return left

            # Otherwise count each element and returns the majority
            left_count = sum(1 for i in range(first, last + 1) if nums[i] == left)
            right_count = sum(1 for i in range(first, last + 1) if nums[i] == right)

            if left_count > right_count:
                return left
            else:
                return right

        return divCon(0, len(nums) - 1)
