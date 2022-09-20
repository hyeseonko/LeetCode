class Solution:
    def bfs(self, row, col):
        queue=[(row, col)]
        self.grid[row][col]=1
        dx=[1,0,0,-1]
        dy=[0,1,-1,0]
        flag=True
        while(queue):
            r, c = queue.pop()
            for z in range(4):
                nr=r+dx[z]
                nc=c+dy[z]
                if (nr in {0, self.m-1} or nc in {0,self.n-1}) and self.grid[nr][nc]==0:
                    flag=False
                elif self.grid[nr][nc]==0:
                    queue.append((nr, nc))
                    self.grid[nr][nc]=1
        return flag
        
    def closedIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.m=len(grid)
        self.n=len(grid[0])
        output = 0
        for i in range(1, self.m-1):
            for j in range(1, self.n-1):
                if self.grid[i][j]==0:
                    if self.bfs(i,j):
                        output+=1
        return output