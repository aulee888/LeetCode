class Solution:
    def merge(self, intervals: list) -> list:
        if not intervals:
            return []

        n = len(intervals)
        output = [intervals[0]]

        def helper(curr_idx):
            if curr_idx > (n - 1):
                return

            a = output[-1][0]
            b = output[-1][1]
            c = intervals[curr_idx][0]
            d = intervals[curr_idx][1]

            # print(f'[{a}, {b}] & [{c}, {d}]')

            # Overlapping 1 --- a < c < b < d
            if a <= c <= b <= d:
                # print('Option 1')
                output.append([a, d])
                output.pop(-2)

            # Overlapping 2 --- c < a < d < b
            elif c <= a <= d <= b:
                output.append([c, b])
                output.pop(-2)

            # No overlap 1 --- a < b < c < d
            elif a <= b < c <= d:
                # print('Option 2')
                output.append([c, d])

            # No overlap 2 --- c < d < a < b
            elif c <= d < a <= b:
                temp = output.pop()
                output.append([c, d])
                output.append(temp)

            # Interval A in B --- c < a < b < d
            elif c <= a <= b <= d:
                # print('Option 3')
                output.append([c, d])
                output.pop(-2)

            # Interval B in Interval A --- a < c < d < b
            # Do nothing; skip over Interval B since A already in output.

            helper(curr_idx + 1)

        helper(1)

        return output


l1 = [[1, 3], [2, 6], [8, 10], [0, 15]]
print(Solution().merge(l1))

