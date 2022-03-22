class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odd = sorted([num for i, num in enumerate(nums) if i%2==1], reverse=True)
        even = sorted([num for i, num in enumerate(nums) if i%2==0], reverse=False)
        output = [None]*len(nums)
        output[::2]=even
        output[1::2]=odd
        return output