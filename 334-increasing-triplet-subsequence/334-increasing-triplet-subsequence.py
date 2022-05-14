class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        dp=[nums[0]]
        for num in nums[1:]:
            if num>dp[-1]:
                dp.append(num)
            elif len(dp)==1 or num<dp[-2]:
                dp[0]=num
            elif num>dp[-2]:
                dp[1]=num
            if len(dp)==3:
                return True
        return False