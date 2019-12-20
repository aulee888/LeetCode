class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        
        for i in range(len(points) - 1):
            current = points[i]
            target = points[i+1]
            
            time += max([abs(target[0] - current[0]), abs(target[1] - current[1])])

        return time
