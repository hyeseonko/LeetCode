class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        len_nums = len(nums)
        for i in range(len_nums-1):
            temp = []
            for j in range(1, len(nums)):
                temp.append((nums[j]+nums[j-1])%10)
            nums = temp
        return nums[0]
            