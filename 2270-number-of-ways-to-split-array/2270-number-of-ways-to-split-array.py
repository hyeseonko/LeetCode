class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        sumnums = sum(nums)
        sofar, output = 0, 0
        for i in range(len(nums)-1):
            sofar+=nums[i]
            if 2*sofar>=sumnums:
                output+=1
        return output