class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        snums = sorted(nums)
        return (snums[-1]-1)* (snums[-2]-1)