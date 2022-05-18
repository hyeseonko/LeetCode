class Solution:
    def numSplits(self, s: str) -> int:
        length = len(s)
        first, last = {}, {}
        
        for k, v in enumerate(s):
            if v not in first:
                first[v] = k
            last[v] = k
            
        first_last = list(first.values())+list(last.values())
        first_last.sort()
        middle = len(first_last)//2
        return first_last[middle]-first_last[middle-1]