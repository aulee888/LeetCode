class Solution:
    ''' Brute Force '''
    def maxArea(self, height: list) -> int:
        max_water = 0

        for i in range(len(height)):

            for j in range(len(height)):
                tops = [height[i], height[j]]

                water = min(tops) * (j-i)

                if water > max_water:
                    max_water = water

        return max_water
        
        
     '''
     Two Pointers
      
     One pointer starts at beginning list, other pointer starts at end of list.
     Due to area being limited by the lower of the two heights, move pointer
     that is with lower height closer to middle
     '''
     def maxArea(self, height: list) -> int:
        max_water = 0
        i = 0
        j = len(height) - 1
        
        while i != j:
            length = min([height[i], height[j]])
            width = j - i
            area = length * width
            
            if area > max_water:
                max_water = area
                
            if height[i] > height[j]:
                 j -= 1
            else:
                 i += 1

        return max_water
