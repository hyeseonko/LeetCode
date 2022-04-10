class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        max_cnt = 0
        for num in set(nums):
            cur_cnt = nums.count(num)
            if cur_cnt > max_cnt:
                max_cnt=cur_cnt
                max_num = [num]
            elif cur_cnt == max_cnt:
                max_num.append(num)
        
        min_path = len(nums)
        for cur_num in max_num:
            cur_indices = [i for i, num in enumerate(nums) if num==cur_num]
            path = cur_indices[-1]-cur_indices[0]+1
            if path<min_path:
                min_path=path
        return min_path