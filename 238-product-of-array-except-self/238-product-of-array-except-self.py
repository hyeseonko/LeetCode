import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_counts = nums.count(0)

        # case 1. the number of '0's >= 2
        if zero_counts>=2:
            return [0]*len(nums)
        
        # case 2. the number of '0's == 1
        elif zero_counts==1:
            zero_index = nums.index(0)
            output = [0]*len(nums)
            nums.remove(0)
            output[zero_index] = math.prod(nums)
            return output
        
        # case 2. the number of '0's == 0
        else:
            prod = math.prod(nums)
            output = [prod//num for num in nums]
            return output