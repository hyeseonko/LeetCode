class Solution:
    def bfs(self, r, c):
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        queue=[(r,c,1)]
        while queue:
            row, col, length = queue.pop(0)
            if self.dp[row][col]<length:
                self.dp[row][col]=length 
            for x, y in zip(dx, dy):
                if row+x in range(self.m) and col+y in range(self.n) and self.matrix[row][col]<self.matrix[row+x][col+y] and self.dp[row+x][col+y]<=length:
                    queue.append((row+x, col+y, length+1))
                    self.dp[row+x][col+y]=length+1
        return length
    
    
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.m, self.n = len(matrix), len(matrix[0])
        self.matrix = matrix
        self.dp = [[1 for _ in range(self.n)] for _ in range(self.m)]
        output = 1
        for i in range(self.m):
            for j in range(self.n):
                if self.dp[i][j]!=1:
                    continue
                o = self.bfs(i, j)
                if o == self.m*self.n:
                    return o
                if o > output:
                    output = o
        return output