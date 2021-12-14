class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx=0
        zeros = nums.count(0)
        nonzeros = len(nums) - zeros
        while(idx<nonzeros):
            if nums[idx]==0:
                nums.pop(idx)
                idx-=1
                nums.append(0)
            idx+=1                