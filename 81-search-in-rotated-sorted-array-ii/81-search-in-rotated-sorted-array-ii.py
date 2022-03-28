class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        return True if target in set(nums) else False