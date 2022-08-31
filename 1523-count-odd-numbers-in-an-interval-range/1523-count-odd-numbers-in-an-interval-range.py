class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high-low)//2 if low%2==0 and high%2==0 else 1+((high-low)//2)