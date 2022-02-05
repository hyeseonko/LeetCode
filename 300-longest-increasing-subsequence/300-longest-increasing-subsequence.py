class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [nums[0]]
        for num in nums[1:]:
            if num > dp[-1]:
                dp.append(num)
            else:
                cur_index = 1
                len_dp = len(dp)
                while(cur_index<=len_dp and num <= dp[-cur_index]):
                    cur_index +=1
                dp[-cur_index+1]=num
        return len(dp)