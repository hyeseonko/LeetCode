class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=3:
            return max(n-2,0)
        
        dp=[0]*n
        start=1
        while(start*start<n):
            start+=1
            if dp[start]==1:
                continue
            for mul in range(start, int((n-1)/start)+1):
                dp[start*mul]=1
        return dp.count(0)-2