class Solution:
    def jump(self, nums: List[int]) -> int:
        len_nums=len(nums)
        dp=[0]*len_nums
        for i, num in enumerate(nums):
            for j in range(1, min(num+1, len_nums)):
                dest=min(i+j, len_nums-1)
                if dp[dest]==0:
                    dp[dest]=1+dp[i]
                else:
                    dp[dest]=min(1+dp[i], dp[dest])
        return dp[-1]