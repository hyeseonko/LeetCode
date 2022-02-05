class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        output = sorted(list(set(nums)), reverse=True)
        try:
            return output[2]
        except IndexError:
            return output[0]