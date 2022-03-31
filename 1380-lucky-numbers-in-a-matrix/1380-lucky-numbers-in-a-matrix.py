class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        candidates = [(i, mat.index(min(mat))) for i, mat in enumerate(matrix)]
        output=[]
        for cand in candidates:
            r, c = cand
            col = [sub[c] for sub in matrix]
            target = matrix[r][c]
            if max(col)==target:
                output.append(target)
        return output