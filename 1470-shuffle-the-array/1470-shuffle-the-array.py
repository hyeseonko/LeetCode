class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return [nums[int(i/2)] if i%2==0 else nums[n+int(i/2)] for i in range(n*2)]