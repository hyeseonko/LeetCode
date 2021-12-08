class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(str(s.split()[-1]))