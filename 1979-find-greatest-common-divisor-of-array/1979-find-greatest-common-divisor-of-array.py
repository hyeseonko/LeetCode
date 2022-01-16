class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_number=min(nums)
        max_number=max(nums)
        if min_number==max_number:
            return min_number
        else:
            while(min_number!=max_number):   
                diff = max_number-min_number
                if min_number%diff==0:
                    return diff
                if min_number>diff:
                    max_number=min_number
                    min_number=diff
                else:
                    max_number=diff
        return 1