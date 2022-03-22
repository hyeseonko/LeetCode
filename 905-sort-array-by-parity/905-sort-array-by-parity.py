class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        elements = sorted([(num%2, num) for num in nums])
        return list(zip(*elements))[1]