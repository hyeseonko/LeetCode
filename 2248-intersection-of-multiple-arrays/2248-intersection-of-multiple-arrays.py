class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        temp = set(nums[0])
        for num in nums[1:]:
            temp = temp.intersection(set(num))
        return sorted(list(temp))