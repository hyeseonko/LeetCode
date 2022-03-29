class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        prev = -1
        for num in sorted(nums):
            if prev == num:
                return num
            prev = num