class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount==0:
            return 1
        else:
            num_coin = len(coins)
            dp=[[0]*num_coin]
            for money in range(1, amount+1):
                output=[0]*num_coin
                for coin_idx in range(num_coin):
                    cur_coin = coins[coin_idx]
                    if money-cur_coin>0:
                        output[coin_idx]=sum(dp[money-cur_coin][coin_idx:])
                    if money==cur_coin:
                        output[coin_idx]=1
                dp.append(output)
            return sum(dp[amount])