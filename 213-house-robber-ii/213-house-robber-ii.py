class Solution:
    def max_dp(self, nums2: List[int]) -> int:
        dp=[0,0,nums2[0]]
        for num in nums2[1:]:
            dp.append(num+max(dp[-2], dp[-3]))
        return max(dp[-1], dp[-2])
            
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=3:
            return max(nums)
        elif len(nums)==4:
            return max(nums[0]+nums[2], nums[1]+nums[-1])
        else:
            dp=[0,0,0]
            cand1 = nums[0]+self.max_dp(nums[2:-1])
            cand2 = nums[-1]+self.max_dp(nums[1:-2])
            cand3 = self.max_dp(nums[1:-1])
            return max(cand1, cand2, cand3)
            
# [1,2,1,0]
# [2,7,9,3,1]