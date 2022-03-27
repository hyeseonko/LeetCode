class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        return sum([1 for i in range(len(heights)) if heights[i]!=expected[i]])