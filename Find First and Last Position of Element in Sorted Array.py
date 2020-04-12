class Solution:
    def searchRange(self, nums: list, target: int) -> list:
        def binary(first, last):
            if first > last:
                return -1

            mid = first + (last - first) // 2  # Minimizes integer overflow

            if target == nums[mid]:
                return mid

            elif target < nums[mid]:
                return binary(first, mid - 1)

            elif target > nums[mid]:
                return binary(mid + 1, last)

        n = len(nums) - 1
        if n == -1:  # Corner case; when list is empty
            return [-1, -1]

        # Divide-and-conquer;
        # Splits the list in two where a target is found.
        init_mid = binary(0, n)

        start = binary(0, init_mid)
        left_check = binary(0, start)

        # + 1 for cases when init_mid is the target.
        # W/o the + 1, we'd never see if end + 1 is also a target value.
        end = binary(init_mid, n)
        right_check = binary(end + 1, n)

        # left_check is pointer that looks for pos of target less than start.
        while left_check < start and left_check != -1:
            start = left_check
            left_check = binary(0, start)

        # right_check is pointer that looks for pos of target greater than end.
        while right_check > end and right_check != -1:
            end = right_check
            right_check = binary(end + 1, n)

        if end < start:  # Corner case; when len(nums) = 1, and target is nums.
            end = start

        return [start, end]
