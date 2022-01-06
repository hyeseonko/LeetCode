class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        mini=nums[0]
        maxj=-1
        output = [-1]
        for num in nums[1:]:
            if num < mini:
                mini=num
                maxj=-1
                continue
            if num > mini and num > maxj:
                maxj = num
            output.append(maxj-mini)
        return max(output)

# [87,68,91,86,58,63,43,98,6,40]