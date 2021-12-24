class Solution:
    def bfs(self, row: int, col: int) -> int:
        num_islands = 0
        stack = [(row, col)]
        self.visited[row][col]=True
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        while(stack):
            cur_row, cur_col = stack.pop(0)
            num_islands+=1
            for x, y in zip(dx, dy):
                if cur_row+x>=0 and cur_row+x<self.m and cur_col+y>=0 and cur_col+y<self.n and not self.visited[cur_row+x][cur_col+y] and self.grid[cur_row+x][cur_col+y]==1:
                    stack.append((cur_row+x, cur_col+y))
                    self.visited[cur_row+x][cur_col+y]=True
        return num_islands
            
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        islands=[0]
        self.visited=[[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])
        for row in range(self.m):
            for col in range(self.n):
                if not self.visited[row][col] and grid[row][col]==1:
                    islands.append(self.bfs(row, col))
                self.visited[row][col]=True
        return max(islands)