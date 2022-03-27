class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return [v for _, v in sorted([(sum(m), i) for i, m in enumerate(mat)])[:k]]
        