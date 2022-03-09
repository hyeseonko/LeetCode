class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        strnums = [str(num) for num in nums]
        strlen = len(nums)
        return [True if int("".join(strnums[:i+1]), 2)%5==0 else False for i in range(strlen)]        