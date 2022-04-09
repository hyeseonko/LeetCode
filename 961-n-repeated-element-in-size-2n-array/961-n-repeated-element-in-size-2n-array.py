class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        len_nums = len(nums)//2
        for x in set(nums):
            if nums.count(x)==len_nums:
                return x