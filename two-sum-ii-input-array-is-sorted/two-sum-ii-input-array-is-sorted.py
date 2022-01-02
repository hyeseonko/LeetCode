class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, num in enumerate(numbers):
            target2 = target - num
            try:
                j = numbers[i+1:].index(target2)
                return [i+1, i+j+2]
            except:
                continue