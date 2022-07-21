class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # similar to coin change
        dp=[1]
        for i in range(1, target+1):
            total = 0
            for num in nums:
                if i-num>=0:
                    total+=dp[i-num]
            dp.append(total)
        return dp[target]