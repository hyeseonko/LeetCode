class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        output=[]
        for num in nums:
            output.append(num*num)
        return sorted(output)
        
        