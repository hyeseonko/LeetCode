class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        for row in range(int(N/2)):
            for col in range(row, N-1-row):
                temp_b = matrix[col][N-1-row]
                temp_c = matrix[N-1-row][N-1-col]
                temp_d = matrix[N-1-col][row]
                matrix[col][N-1-row]=matrix[row][col]
                matrix[N-1-row][N-1-col] = temp_b
                matrix[N-1-col][row] = temp_c
                matrix[row][col] = temp_d
        return matrix