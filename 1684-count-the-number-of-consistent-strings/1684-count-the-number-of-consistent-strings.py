class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        result=0
        for word in words:
            cur = set(c for c in word)
            checked=False
            for each in cur:
                if each not in allowed:
                    checked=True
                    break
            if not checked:
                result+=1
        return result