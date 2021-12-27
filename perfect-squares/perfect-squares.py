class Solution:
    def numSquares(self, n: int) -> int:
        bases = [i**2 for i in range(1,101)] # [1,4,9,16,...]
        dp=[0,1,2,3,1]
        for i in range(5, n+1):
            # case 1. perfect squares
            if i in bases:
                dp.append(1)
                continue
            # case 2. not perfect squares
            candidates=[]
            for b in bases:
                if b>=i:
                    break
                candidates.append(dp[i-b])
            dp.append(1+min(candidates))
        return dp[n]