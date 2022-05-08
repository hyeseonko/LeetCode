class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # Three quick failure cases
        if grid[0][0]==")": return False
        if grid[-1][-1]=="(": return False
        if (m+n)%2==0: return False
        
        # Let's start!
        queue=[(0,0,1)] # row, col, acc.sum (must be 0 at the destination); assuming that "("=1 and ")"=-1
        visited=set()
        visited.add((0,0,1))
        while(queue):
            row, col, acc_sum = queue.pop(0)
            if row==m-1 and col==n-1 and acc_sum==0:
                return True
            
            # move down
            if row < m-1:
                next_item=1 if grid[row+1][col]=="(" else -1
                next_sum = acc_sum+next_item
                if next_sum>=0 and (row+1, col, next_sum) not in visited:
                    queue.append((row+1, col, next_sum))
                    visited.add((row+1, col, next_sum))
            
            # move right
            if col < n-1:
                next_item=1 if grid[row][col+1]=="(" else -1
                next_sum = acc_sum+next_item
                if next_sum>=0 and (row, col+1, next_sum) not in visited:
                    queue.append((row, col+1, next_sum))
                    visited.add((row, col+1, next_sum))
        return False