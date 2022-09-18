class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        output = 0
        dp = [0, 0] # positive, negative
        for num in nums:
            if num>0:
                dp[0]+=1
                dp[1]+=1 if dp[1]!=0 else 0
            elif num<0:
                temp=dp[0]+1
                dp[0]=dp[1]+1 if dp[1]!=0 else 0
                dp[1]=temp
            else:
                dp=[0, 0]
                continue
            if dp[0]>output:
                output = dp[0]
        return output