class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        row=[0]*m
        col=[0]*n
        for r, c in indices:
            row[r]+=1
            col[c]+=1
        result=0
        for r in row:
            for c in col:
                if (r+c)%2==1:
                    result+=1
        return result