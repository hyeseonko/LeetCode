class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        output = sum([mat[i][i]+mat[i][n-1-i] if n!=2*i+1 else mat[i][i] for i in range(n)])
        return output