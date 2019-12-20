class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels_list = []
        count = 0
        
        for jewel in J:
            jewels_list.append(jewel)
        
        for stone in S:
            if stone in jewels_list:
                count += 1
                
        return count
