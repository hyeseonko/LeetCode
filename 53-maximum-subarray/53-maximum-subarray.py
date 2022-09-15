class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp=[]
        dp.append(nums[0])
        for num in nums[1:]:
            dp.append(max(num, dp[-1]+num))
        return max(dp)