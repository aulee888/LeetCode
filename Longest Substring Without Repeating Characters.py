class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ''
        
        for i in range(len(s)):
            temp_string = ''
            
            for j in range(i, len(s)):
                
                if s[j] not in temp_string:
                    temp_string = temp_string + s[j]
                    
                else: break
                    
            if len(temp_string) > len(substring):
                substring = temp_string
                
        return len(substring)
