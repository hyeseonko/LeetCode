class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        # method 2. Recursive O(logN)
        output = 0
        x = 5
        while x<=n:
            output += n//x
            x *= 5
        return output
        
        
        return output
        
        # method 1. DP O(N)
        # dp = [0,0,0,0,0]
        # for num in range(5, n+1):
        #     if num%5==0:
        #         dp.append(num//5 + dp[num//5])
        #     else:
        #         dp.append(dp[-1])
        # return dp[n]