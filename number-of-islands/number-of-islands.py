class Solution:
    def bfs(self, row: int, col: int) -> None:
        stack=[(row, col)]
        while(stack):
            cur_row, cur_col = stack.pop(0)
            if cur_row<self.m-1 and not self.visited[cur_row+1][cur_col] and self.grid[cur_row+1][cur_col]=="1":
                stack.append((cur_row+1, cur_col))
                self.visited[cur_row+1][cur_col]=True
            if cur_col<self.n-1 and not self.visited[cur_row][cur_col+1] and self.grid[cur_row][cur_col+1]=="1":
                stack.append((cur_row, cur_col+1))
                self.visited[cur_row][cur_col+1]=True
            if cur_col>0 and not self.visited[cur_row][cur_col-1] and self.grid[cur_row][cur_col-1]=="1":
                stack.append((cur_row, cur_col-1))
                self.visited[cur_row][cur_col-1]=True
            if cur_row>0 and not self.visited[cur_row-1][cur_col] and self.grid[cur_row-1][cur_col]=="1":
                stack.append((cur_row-1, cur_col))
                self.visited[cur_row-1][cur_col]=True    
        
    def numIslands(self, grid: List[List[str]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        self.grid = grid
        islands=0
        self.visited=[[False for _ in range(self.n)] for _ in range(self.m)]
        for row in range(self.m):
            for col in range(self.n):
                if not self.visited[row][col] and grid[row][col]=="1":
                    self.visited[row][col]=True
                    self.bfs(row, col)
                    islands+=1
        
        return islands
                    
            
        
        