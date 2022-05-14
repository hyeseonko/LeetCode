class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        snums = sorted(nums)
        return sum([snums[2*i] for i in range(len(snums)//2)])