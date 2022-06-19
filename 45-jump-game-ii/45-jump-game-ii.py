class Solution:
    def jump(self, nums: List[int]) -> int:
        
        # dp[i] = minimum number of jumps so far
        len_nums = len(nums)
        dp=[0]*len_nums
        for i, num in enumerate(nums):
            for jump in range(1, min(1+num, len_nums)):
                landed = i + jump
                if landed >= len_nums:
                    break
                if dp[landed]==0:
                    dp[landed]=dp[i]+1
                else:
                    dp[landed]=min(dp[landed], 1+dp[i])
        return dp[-1]                
        
        
        # len_nums=len(nums)
        # dp=[0]*len_nums
        # for i, num in enumerate(nums):
        #     for j in range(1, min(num+1, len_nums)):
        #         dest=min(i+j, len_nums-1)
        #         if dp[dest]==0:
        #             dp[dest]=1+dp[i]
        #         else:
        #             dp[dest]=min(1+dp[i], dp[dest])
        # return dp[-1]