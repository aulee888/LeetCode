class Solution:
    def isValid(self, s: str) -> bool:
        paren = {'(': ')', '[': ']', '{': '}'}
        valid = True
        char = []

        for i in range(len(s)):
            if s[i] in '({[':
                char.append(s[i])

            else:
                if char == []:
                    valid = False
                    
                else:
                    if paren[char.pop()] != s[i]:
                        valid = False

                        break
                        
        if char != []:
            valid = False

        return valid
