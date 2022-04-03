class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(set(s))!=len(set(t)): return False
        di = dict()
        for left, right in zip(s, t):
            if left not in di:
                di[left]=right
            elif di[left]!=right:
                return False
        return True
                