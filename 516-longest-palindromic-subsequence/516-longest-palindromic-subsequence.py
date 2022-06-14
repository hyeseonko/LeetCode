class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        w1, w2 = s, s[::-1]
        m = len(w1)
        dp=[[0]*(m+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(m):
                dp[i+1][j+1]=max(dp[i][j+1], dp[i+1][j], dp[i][j]+(w1[i]==w2[j]))
        return dp[m][m]