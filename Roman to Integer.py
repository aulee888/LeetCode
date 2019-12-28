class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000
        }
        
        i = 0
        convert = 0
        
        while i < len(s):
            if (s[i] in ['I', 'X', 'C'] and 
                    (i != (len(s) - 1) and s[i] + s[i+1] in roman)):
                           
                numeral = s[i] + s[i+1]
                convert += roman[numeral]
                
                i += 2
                
            else:
                convert += roman[s[i]]
                
                i += 1
                
        return convert
