class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        output=[[0 for _ in range(n)] for _ in range(n)]
        cand = set()
        for i in range(n):
            for j in range(n):
                output[j][i]=grid[i][j]

        result=0
        for row in grid:
            for col in output:
                if row == col:
                    result+=1
        return result
                    