class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        starts = [i for i, c in enumerate(s) if c==goal[0]]
        for start in starts:
            if s[start:]+s[:start]==goal:
                return True
        return False