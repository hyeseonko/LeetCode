class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = [num for num in nums if num%2==0]
        odd = [num for num in nums if num%2==1]
        output=[None]*len(nums)
        output[::2]=even
        output[1::2]=odd
        return output