class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # method 1. Forward
        # last_position = 0
        # for i, num in enumerate(nums):
        #     if i > last_position:
        #         return False
        #     last_position = max(last_position, i+num)
        # return True

        # method 2. Backward
        last_position = len(nums)-1
        for i in range(last_position-1, -1, -1):
            if (i+nums[i])>=last_position:
                last_position = i
        return last_position == 0