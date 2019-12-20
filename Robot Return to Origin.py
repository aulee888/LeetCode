class Solution:
    def judgeCircle(self, moves: str) -> bool:
        position = [0, 0]
        
        for move in moves:
            if move == 'U':
                position[0] += 1
            elif move == 'D':
                position[0] -= 1
            elif move == 'L':
                position [1] -= 1
            elif move == 'R':
                position[1] += 1
                
        if position == [0, 0]:
            return True
        else:
            return False
