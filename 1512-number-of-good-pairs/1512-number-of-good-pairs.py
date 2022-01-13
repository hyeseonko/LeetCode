class Solution:
    def combination(self, a: int) -> int:
        return int(a*(a-1)/2)
    def numIdenticalPairs(self, nums: List[int]) -> int:
        result=0
        for num in set(nums):
            num_count = nums.count(num)
            if num_count>1:
                result+=self.combination(num_count)
        return result