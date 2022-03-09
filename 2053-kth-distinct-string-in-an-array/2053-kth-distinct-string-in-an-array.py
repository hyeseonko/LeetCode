class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        output = [c for c in arr if arr.count(c)==1]
        try:
            return output[k-1]
        except:
            return ""