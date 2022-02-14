class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        len_indices = len(indices)
        return "".join(s[indices.index(i)] for i in range(len_indices))