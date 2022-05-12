class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        lens=len(s)
        for i in range(1, lens//2+1):
            if lens%i==0 and s[:i]*(lens//i)==s:
                return True
        return False