class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        A = sum(nums)
        acc_num=0
        for i, num in enumerate(nums):
            if A==num+2*acc_num:
                return i
            acc_num+=num
        return -1