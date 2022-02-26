class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        samefreq = s.count(s[0])
        for c in set(s):
            if s.count(c)!=samefreq:
                return False
        return True