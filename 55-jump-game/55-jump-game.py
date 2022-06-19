class Solution:
    def canJump(self, nums: List[int]) -> bool:
        m = 0
        for i, n in enumerate(nums):
            if i > m:
                return False
            m = max(m, i+n)
        return True
        
#         len_nums=len(nums)
#         dp=[False for _ in range(len_nums)]
#         dp[0]=True
#         for i, num in enumerate(nums):
#             if dp[-1]:
#                 return True
#             if num==0 or dp[i]==False:
#                 continue
#             for j in range(num, 0, -1):
#                 dp[min(i+j, len_nums-1)]=True
                
#         return dp[-1]