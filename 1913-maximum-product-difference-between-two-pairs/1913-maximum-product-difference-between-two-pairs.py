class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        snum = sorted(nums)
        return snum[-1]*snum[-2]-snum[0]*snum[1]