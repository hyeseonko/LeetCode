class Solution:
    def arrangeCoins(self, n: int) -> int:
        k = 1
        while True:
            if (k**2+k)//2 > n:
                return k-1
            k+=1
            
        