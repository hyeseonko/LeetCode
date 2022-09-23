class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        snums = set(nums)
        return len(snums) if 0 not in snums else len(snums)-1
        