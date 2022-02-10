class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output=[nums[0]]
        for num in nums[1:]:
            output.append(num+output[-1])
        return output