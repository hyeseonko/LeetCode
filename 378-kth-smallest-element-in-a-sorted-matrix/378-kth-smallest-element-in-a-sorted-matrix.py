class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        A = [matrix[i][j] for i in range(len(matrix)) for j in range(len(matrix))]
        return sorted(A)[k-1]