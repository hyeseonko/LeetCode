class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(n^2)
        # for i, num in enumerate(nums[:-1]):
        #     for j in range(i+1, len(nums)):
        #         if num+nums[j]==target:
        #             return [i,j]
        
        # O(n)
        waiting_dict = {}
        for i in range(len(nums)):
            if nums[i] in waiting_dict:
                return [waiting_dict[nums[i]], i]
            else:
                waiting_dict[target-nums[i]]=i