class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # solution1. O(n**2)
        for i, num in enumerate(nums):
            for j, num2 in enumerate(nums):
                if num+num2==target and i!=j:
                    return [i, j]
            
        