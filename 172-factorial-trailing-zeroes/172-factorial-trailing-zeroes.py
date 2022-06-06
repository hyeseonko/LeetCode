class Solution:
    def trailingZeroes(self, n: int) -> int:
        dp = [0,0,0,0,0]
        for num in range(5, n+1):
            if num%5==0:
                dp.append(num//5 + dp[num//5])
            else:
                dp.append(dp[-1])
        return dp[n]