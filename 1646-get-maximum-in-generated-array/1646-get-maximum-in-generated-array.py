class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        dp=[0,1]
        for i in range(2, n+1):
            if i%2==0:
                dp.append(dp[int(i/2)])
            else:
                dp.append(dp[int(i/2)]+dp[int(i/2)+1])
        return max(dp[:n+1])