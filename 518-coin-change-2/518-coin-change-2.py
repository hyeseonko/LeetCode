class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # method 2. DP using 1d space; dp[i]
        dp = [1] + [0]*amount
        for coin in coins:
            for i in range(1, amount+1):
                if i>=coin:
                    dp[i]+=dp[i-coin] # key idea
        return dp[-1]
        
        # method 1. DP using 2d space; dp[i][j]
        # if amount==0:
        #     return 1
        # else:
        #     num_coin = len(coins)
        #     dp=[[0]*num_coin]
        #     for money in range(1, amount+1):
        #         output=[0]*num_coin
        #         for coin_idx in range(num_coin):
        #             cur_coin = coins[coin_idx]
        #             if money-cur_coin>0:
        #                 output[coin_idx]=sum(dp[money-cur_coin][coin_idx:])
        #             if money==cur_coin:
        #                 output[coin_idx]=1
        #         dp.append(output)
        #     return sum(dp[amount])