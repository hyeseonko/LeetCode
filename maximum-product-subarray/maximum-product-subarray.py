class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        if nums[0]>=0:
            dp_plus=[nums[0]]
            dp_minus=[0]
        else:
            dp_plus=[0]
            dp_minus=[nums[0]]
        for i, num in enumerate(nums[1:]):
            if num==0:
                dp_plus.append(0)
                dp_minus.append(0)
            elif num>0:
                dp_plus.append(max(num, num*dp_plus[i]))
                dp_minus.append(min(0, num*dp_minus[i]))
            else:
                dp_plus.append(max(0, num*dp_minus[i]))
                dp_minus.append(min(num, num*dp_plus[i]))

        return max(dp_plus)
        