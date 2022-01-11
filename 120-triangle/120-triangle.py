class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp=[triangle[0][0]]
        for row_list in triangle[1:]:
            # From backwards, value won't be affected.
            dp.append(row_list[-1]+dp[-1])
            len_row = len(row_list)
            for i in range(-2,-(len_row), -1):
                dp[i]=row_list[i]+min(dp[i], dp[i-1])
            dp[0]+=row_list[0]
        return min(dp)