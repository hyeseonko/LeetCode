class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        num_row = len(matrix)
        prev_dp=[]
        prev_dp+=[x for x in matrix[0]]     # first row
        cur_dp=[matrix[0][0]]*num_row       # to handle the case of 1x1 matrix
        for row in matrix[1:]:
            cur_dp[0]=row[0]+min(prev_dp[0], prev_dp[1])
            cur_dp[-1]=row[-1]+min(prev_dp[-1], prev_dp[-2])
            for col in range(1,num_row-1):
                cur_dp[col]=row[col]+min(prev_dp[col-1], prev_dp[col], prev_dp[col+1])
            prev_dp=cur_dp[:] # copy only values from the list
        return min(cur_dp)