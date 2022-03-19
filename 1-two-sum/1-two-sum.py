class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums[:-1]):
            for j in range(i+1, len(nums)):
                if num+nums[j]==target:
                    return [i,j]