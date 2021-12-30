class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[0]
        for i in range(1,amount+1):
            cur=[]
            if i in coins:
                dp.append(1)
            else:
                candidate=[]
                for coin in coins:
                    if i-coin>0 and dp[i-coin]!=-1:
                        candidate.append(dp[i-coin])
                if not candidate:
                    dp.append(-1)
                else:
                    dp.append(1+min(candidate))
        return dp[-1]
        