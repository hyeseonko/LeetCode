class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numdict={i: nums.count(i) for i in range(3)}
        cur=0
        for i in range(len(nums)):
            while(numdict[cur]==0):
                cur+=1
            nums[i]=cur
            numdict[cur]-=1