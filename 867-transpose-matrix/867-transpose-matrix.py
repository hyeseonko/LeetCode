class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        output = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(m):
            for j in range(n):
                output[j][i]=matrix[i][j]
        return output