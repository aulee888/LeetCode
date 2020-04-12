class Solution:
    def addBinary(self, a, b):
        def fromBinary(x):
            """
            Turns a binary string to an integer.
            Iterates through the from left to right.
            Leftmost character is exponent:len(x) - 1, where rightmost char exp:0.
            """
            result = 0
            exponent = len(x) - 1

            for i in range(len(x)):
                if x[i] == '1':
                    result += 2 ** exponent

                exponent -= 1

            return result

        def toBinary(x):
            """
            Converts an int to a binary string.
            Looks for an i such that 2**i > x.
            i-1 removes an extra 0 that would appear in front of binary string.
            If 2**i <= x, then append 1, else append 0 integrity of binary string
            is maintained.
            If you were to only append and not append 0's, you'd be missing enough
            digits to make up your int as a binary string.
            """
            if x == 0:
                return "0"

            result = ""
            i = 0

            while 2 ** i <= x:
                i += 1

            i -= 1

            while i >= 0:
                if 2 ** i <= x:
                    x -= 2 ** i
                    result = result + '1'

                else:
                    result = result + '0'
                i -= 1

            return result

        return toBinary(fromBinary(a) + fromBinary(b))
