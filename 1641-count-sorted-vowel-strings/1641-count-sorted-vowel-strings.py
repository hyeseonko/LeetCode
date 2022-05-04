class Solution:
    def countVowelStrings(self, n: int) -> int:
        # dp[0] = ending with 'a'
        # dp[1] = ending wiht 'e'
        # dp[2] = ending with 'i'
        # dp[3] = ending with 'o'
        # dp[4] = ending with 'u'
        dp=[1,1,1,1,1]
        for i in range(2, n+1):
            dp[4]+=dp[3]+dp[2]+dp[1]+dp[0]
            dp[3]+=dp[2]+dp[1]+dp[0]
            dp[2]+=dp[1]+dp[0]
            dp[1]+=dp[0]
        return sum(dp)