class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        counts = 0
        for i in range(len(nums)-1):
            base = nums[i]
            for j in range(i+1, len(nums)):
                compare = nums[j]
                if base-compare==k or base-compare==-k:
                    counts+=1
        return counts
        