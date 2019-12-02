class Solution:
    def isPalindrome(self, x: int) -> bool:
        list = []
        output = ''
        x = str(x)

        for i in range(len(x)):
            list.append(x[i])

        for j in range(len(x)):
            output = output + list.pop() 

        if output == x:
            return True
        else:
            return False
