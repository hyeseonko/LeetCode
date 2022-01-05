class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_dp, sell_dp, output = prices[0],prices[0], {0}
        for val in prices:
            if val < buy_dp:
                buy_dp=val
                sell_dp=val
            elif val > sell_dp:
                sell_dp=val
            output.add(sell_dp-buy_dp)
        return max(output)