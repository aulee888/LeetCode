class Solution:
    def search(self, nums: list, target: int) -> int:
        def binary(start, end):
            if start > end:  # Corner case; target not in list
                return -1

            mid = (start + end) // 2

            if nums[mid] == target:  # Base case
                return mid

            # Divide and conquer + recursive binary search
            # Differs from plain binary sort by checking to see if a number is
            # in a half; the half may be out of order/rotated.
            # A plain binary sort would say a number doesn't exist in list due
            # to rotation, when it really may be in the other half.
            if nums[mid] < nums[end]:  # Right is in ascending order
                if nums[mid] < target <= nums[end]:
                    return binary(mid + 1, end)  # Search right half
                else:
                    return binary(start, mid - 1)  # Search left half

            else:  # Left is in ascending order
                if nums[start] <= target < nums[mid]:
                    return binary(start, mid - 1)  # Search left half
                else:
                    return binary(mid + 1, end)  # Search right half

        return binary(0, len(nums) - 1)

