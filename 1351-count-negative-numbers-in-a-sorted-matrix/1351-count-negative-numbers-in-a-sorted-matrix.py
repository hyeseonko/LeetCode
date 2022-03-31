class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        col_len = len(grid[0])
        output=0
        for row in grid:
            for i, val in enumerate(row):
                if val<0:
                    output+=(col_len-i)
                    break
        return output