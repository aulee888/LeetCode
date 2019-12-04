class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        
        if -2**31 <= x < 2**31 and x != 0:
            
            if x < 0:
                negative = True
                x = abs(x)

            rev = ''
            while x != 0:
                rev = rev + str(x % 10)
                x = x // 10

            if negative:
                rev = '-' + rev
            
            if -2**31 <= int(rev) < 2**31:
                return int(rev)
            else:
                return 0
         
        else:
            return 0
