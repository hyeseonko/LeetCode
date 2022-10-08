class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        items = sorted(items1+items2)
        result = []
        prev_k, prev_v = None, 0
        for k, v in items:
            if prev_k is not None and k!=prev_k:
                result.append([prev_k, prev_v])
                prev_v = 0
            
            prev_k = k
            prev_v += v
        
        result.append([prev_k, prev_v])
        return result