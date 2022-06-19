class Solution:
    # method 1. DFS (recursive) without using visited
    def dfs(self, x, y):
        # exit condition
        if not (x in range(self.m) and y in range(self.n)) or self.grid[x][y]=="0":
            return
        # proceed
        self.grid[x][y]="0"
        self.dfs(x+1, y)
        self.dfs(x, y+1)
        self.dfs(x, y-1)
        self.dfs(x-1, y)
        
    def numIslands(self, grid: List[List[str]]) -> int:
        output = 0
        self.grid = grid
        self.m, self.n = len(grid), len(grid[0])
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j]=="1":
                    self.dfs(i, j)
                    output+=1
        return output

    # method 2. BFS (queue)
#     def bfs(self, x, y):
#         queue = [(x, y)]
#         self.grid[x][y]=="0"
#         dx = [0, 0, 1, -1]
#         dy = [1, -1, 0, 0]
#         while queue:
#             curx, cury = queue.pop(0)
#             for i in range(4):
#                 nextx, nexty = curx + dx[i], cury + dy[i]
#                 if nextx in range(self.m) and nexty in range(self.n) and self.grid[nextx][nexty]=="1":
#                     queue.append((nextx, nexty))
#                     self.grid[nextx][nexty]="0"

#     def numIslands(self, grid: List[List[str]]) -> int:
#         output = 0
#         self.grid = grid
#         self.m, self.n = len(grid), len(grid[0])
#         for i in range(self.m):
#             for j in range(self.n):
#                 if grid[i][j]=="1":
#                     self.bfs(i, j)
#                     output+=1
#         return output

        