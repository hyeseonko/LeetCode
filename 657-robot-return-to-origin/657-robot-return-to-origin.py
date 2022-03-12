class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if len(set(moves))%2==1:
            return False
        origin=[0, 0]
        direction = {"R": [1, 0], "L": [-1, 0], "U": [0, 1], "D": [0, -1]}
        for move in moves:
            origin[0]+=direction[move][0]
            origin[1]+=direction[move][1]
        if origin==[0,0]:
            return True
        else:
            return False