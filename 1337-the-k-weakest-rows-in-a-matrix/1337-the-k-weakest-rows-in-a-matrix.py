class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        sumMat = [[row, i] for i, row in enumerate(mat)]
        sumMat.sort(key=lambda x: sum(x[0]))
        return [i for _, i in sumMat[:k]]