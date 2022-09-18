class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        ariset=set(nums)
        output=0
        for num in nums:
            if num+diff in ariset and num+2*diff in ariset:
                output+=1
        return output
        