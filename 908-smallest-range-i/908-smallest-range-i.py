class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        diff = max(nums)-min(nums)
        return max(0, diff-2*k)