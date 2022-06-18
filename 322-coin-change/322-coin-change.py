class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0]
        for i in range(1, amount+1):
            candidate = [dp[i-coin] for coin in coins if i-coin>=0 and dp[i-coin]!=-1]
            dp+=[min(candidate)+1 if candidate else -1]
        return dp[-1]