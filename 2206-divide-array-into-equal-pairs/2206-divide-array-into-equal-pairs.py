class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq = {n: nums.count(n) for n in set(nums)}
        output = 0
        for _, v in freq.items():
            output+=v//2
        if output==len(nums)//2:
            return True
        else:
            return False