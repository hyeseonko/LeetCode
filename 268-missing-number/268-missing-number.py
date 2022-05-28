class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return list(set(range(len(nums)+1))-set(nums))[0]