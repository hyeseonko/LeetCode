class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1: return -1
        queue=[(0, 0, 1)]
        n = len(grid)
        visited=[[False for _ in range(n)] for _ in range(n)]
        dx = [-1,-1,-1,0,0,1,1,1]
        dy = [-1,0,1,-1,1,-1,0,1]
        while queue:
            r, c, curlen = queue.pop(0)
            if r==n-1 and c==n-1:
                return curlen
            for x, y in zip(dx, dy):
                if r+x>=0 and r+x<n and c+y>=0 and c+y<n and not visited[r+x][c+y] and grid[r+x][c+y]==0:
                    visited[r+x][c+y]=True
                    queue.append((r+x, c+y, curlen+1))
        return -1