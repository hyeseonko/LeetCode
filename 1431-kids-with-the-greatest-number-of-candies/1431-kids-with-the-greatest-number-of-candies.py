class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxcandy = max(candies)
        return [True if candy+extraCandies>=maxcandy else False for candy in candies]
        