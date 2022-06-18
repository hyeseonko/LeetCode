class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # method 1. cascading
        output = [[]]
        
        for num in nums:
            output += [o + [num] for o in output]
        
        return output