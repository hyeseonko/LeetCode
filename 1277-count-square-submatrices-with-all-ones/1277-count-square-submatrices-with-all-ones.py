class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(n):
            dp[0][i]=matrix[0][i]
        for j in range(m):
            dp[j][0]=matrix[j][0]
        for row in range(1, m):
            for col in range(1, n):
                if matrix[row][col]==0:
                    dp[row][col]=0
                else:
                    dp[row][col]=1+min(dp[row-1][col], dp[row][col-1], dp[row-1][col-1])
        return sum([sum(x) for x in dp])