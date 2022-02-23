class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        return [i for i, x in enumerate(sorted(nums)) if x == target]