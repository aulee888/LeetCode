class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        
        if strs != []:
            shortest = strs[0]
        
            for string in strs:
                if len(string) < len(shortest):
                    shortest = string
            
            for i in range(len(shortest)):
                letter = strs[0][i]

                for string in strs:

                    if string[i] != letter:
                        return prefix

                prefix = prefix + letter
        
        return prefix
