class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        buy=prices[0]
        for price in prices[1:]:
            if buy<price:
                profit+=price-buy
            buy = price
        return profit