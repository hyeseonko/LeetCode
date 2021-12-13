class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp=[1 for _ in range(rowIndex+1)]
        for row in range(2, rowIndex+1):
            for idx in range(row-1, 0, -1):
                dp[idx]+=dp[idx-1]
        return dp
        