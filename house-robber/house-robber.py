class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<3:
            return max(nums)
        elif len(nums)==3:
            return max(nums[1], nums[0]+nums[2])
        else:
            dp=[nums[0], nums[1], nums[2]+nums[0]]
            for num in nums[3:]:
                dp.append(max(dp[-2], dp[-3])+num)
            return max(dp[-1], dp[-2])