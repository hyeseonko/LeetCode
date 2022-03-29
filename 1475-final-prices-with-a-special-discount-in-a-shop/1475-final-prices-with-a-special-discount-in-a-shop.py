class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result=[]
        for i in range(len(prices)-1):
            flag=False
            for j in range(i+1, len(prices)):
                if prices[i] >= prices[j]:
                    result.append(prices[i]-prices[j])
                    flag=True
                    break
            if not flag:
                result.append(prices[i])
        result.append(prices[-1])
        return result