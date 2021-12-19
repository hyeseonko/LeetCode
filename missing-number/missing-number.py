class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        maxnum = len(nums)
        for i in range(maxnum+1):
            if i not in nums:
                return i
        