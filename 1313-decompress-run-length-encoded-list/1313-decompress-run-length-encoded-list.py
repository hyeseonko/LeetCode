class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        _len = len(nums)//2
        output=[]
        for i in range(_len):
            output+=[nums[2*i+1]]*nums[2*i]
        return output