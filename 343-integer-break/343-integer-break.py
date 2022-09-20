class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [1, 1, 1]
        for num in range(3, n+1):
            cur=[]
            for i in range(2, num):
                cur.append(max(i*dp[num-i], i*(num-i)))            
            dp.append(max(cur))
        return dp[n]
        