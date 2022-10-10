class Solution:
    def numTrees(self, n: int) -> int:
        dp=[1,1]
        for i in range(2, n+1):
            result=0
            for j in range(i):
                result+=dp[j]*dp[i-j-1]
            dp.append(result)
        return dp[n]