class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        if grid[0][0] == ')':
            return False
        queue = deque([(0, 0, 1)])
        visited = set([0, 0, 1])
        while queue:
            x, y, paran = queue.popleft()
            if x == len(grid) - 1 and y == len(grid[0]) - 1 and paran == 0:
                return True
            for i, j in (1, 0), (0, 1):
                x1, y1 = x + i, y + j
                if 0 <= x1 < len(grid) and 0 <= y1 < len(grid[0]):
                    new_paran = paran + (1 if grid[x1][y1] == '(' else -1)
                    if (x1, y1, new_paran) in visited or new_paran < 0:
                        continue
                    visited.add((x1, y1, new_paran))
                    queue.append((x1, y1, new_paran))
        return False

# class Solution:
#     def isValid(self, path) -> bool:
#         # ['(', ')', '(', '(', ')', ')']
#         stack=[path[0]]
#         for p in path[1:]:
#             if p=="(":
#                 stack.append(p)
#             else:
#                 if stack and stack[-1]=="(":
#                     stack.pop(-1)
#                 else:
#                     stack.append(p)
#         return not stack
        
        
#     def hasValidPath(self, grid: List[List[str]]) -> bool:
#         m, n = len(grid), len(grid[0])
#         if grid[0][0]==")": return False
#         if grid[-1][-1]=="(": return False
#         if (m+n-1)%2!=0: return False
#         queue=[([grid[0][0]], 0, 0, 1, 0)]
#         while queue:
#             curpath, r, c, front_count, back_count = queue.pop(0)
#             if r==m-1 and c==n-1:
#                 if self.isValid(curpath):
#                     return True
#                 continue
#             if front_count<back_count or front_count>(m+n-1)//2 or back_count>=(m+n-1)//2:
#                 continue
#             if r<m-1:
#                 if grid[r+1][c]=="(":
#                     queue.append((curpath+[grid[r+1][c]], r+1, c, front_count+1, back_count))
#                 else:
#                     queue.append((curpath+[grid[r+1][c]], r+1, c, front_count, back_count+1))
#             if c<n-1:
#                 if grid[r][c+1]=="(":
#                     queue.append((curpath+[grid[r][c+1]], r, c+1, front_count+1, back_count))
#                 else:
#                     queue.append((curpath+[grid[r][c+1]], r, c+1, front_count, back_count+1))

#         return False