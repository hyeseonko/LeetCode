class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        # starting point: column-wise [0, n)
        for col in range(n):
            num = matrix[0][col]
            (r, c) = (0, col)
            while(r<m and c<n):
                if matrix[r][c]!=num:
                    return False
                r+=1
                c+=1           
        # starting point: row-wise [1, m)
        for row in range(m):
            num = matrix[row][0]
            (r, c) = (row, 0)
            while(r<m and c<n):
                if matrix[r][c]!=num:
                    return False
                r+=1
                c+=1
        return True