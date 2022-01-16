class Solution:
    def countBits(self, n: int) -> List[int]:
        dp=[0,1,1,2,1,2]
        for i in range(6,n+1):
            dp.append(dp[int(i/2)]+dp[i%2])
        
        return dp[:n+1]
        