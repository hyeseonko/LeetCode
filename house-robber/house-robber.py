class Solution:
    def rob(self, nums: List[int]) -> int:
        dp=[0, 0, nums[0]]
        for num in nums[1:]:
            dp.append(num+max(dp[-2], dp[-3]))
        return max(dp[-1], dp[-2])