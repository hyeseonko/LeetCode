class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp=[[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                dp[row][col]=grid[row][col]
                if row==0 and col==0:
                    continue
                candidates=set()
                if col>0:
                    candidates.add(dp[row][col-1])
                if row>0:
                    candidates.add(dp[row-1][col])
                dp[row][col]+=min(candidates)
        return dp[-1][-1]