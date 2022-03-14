class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = [num+1 for num in range(len(matrix))]
        length = len(matrix)
        for i in range(length):
            col = [matrix[j][i] for j in range(length)]
            for num in n:
                if num not in matrix[i] or num not in col:
                    return False
        return True