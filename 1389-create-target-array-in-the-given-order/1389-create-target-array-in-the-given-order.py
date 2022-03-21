class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        output=[]
        for i, num in enumerate(nums):
            output.insert(index[i], num)
        return output
        