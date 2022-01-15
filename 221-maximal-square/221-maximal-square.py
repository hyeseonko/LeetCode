import math

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp=[[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row==0 or col==0 or matrix[row][col]=="0":
                    dp[row][col]=int(matrix[row][col])
                else:
                    min_value = min(int(dp[row-1][col]), int(dp[row][col-1]), int(dp[row-1][col-1]))
                    dp[row][col]=pow(int(sqrt(min_value))+1, 2)

        return max(map(max, dp))