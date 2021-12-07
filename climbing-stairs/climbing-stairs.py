class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[1,2]
        for _ in range(max(0, n-2)):
            dp.append(dp[-1]+dp[-2])
        return dp[n-1]
        