class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums)<3:
            return 0
        output=[]
        slices=[nums[0], nums[1]]
        for num in nums[2:]:
            if num-slices[-1]==slices[1]-slices[0]:
                slices.append(num)
            else:
                if len(slices)>=3:
                    output.append(slices)
                slices=[slices[-1], num]
        output.append(slices)
        result = 0
        for o in output:
            result+= int((len(o)-2)*(len(o)-1)/2)
        return result