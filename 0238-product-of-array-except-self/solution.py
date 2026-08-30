class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer, suffix, prefix = [1]*len(nums), 1, 1
        for i in range(len(nums)):
            answer[i]*=prefix
            prefix*=nums[i]
            answer[-i-1]*=suffix
            suffix*=nums[-i-1]
        
        return answer
