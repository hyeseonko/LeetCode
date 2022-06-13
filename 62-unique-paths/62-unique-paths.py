class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Combinatorics: (m-1)+(n-1) C min(m-1,n-1)
        # output=1
        # bunmo=1
        # for i, bunja in enumerate(range(m+n-2, max(m,n)-1,-1), 1):
        #     output*=bunja
        #     bunmo*=i
        # return output//bunmo
    
        # DP
        dp=[[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            dp[i][0]=1
        for j in range(n):
            dp[0][j]=1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]