class Solution:
    def repeatedCharacter(self, s: str) -> str:
        visited=set()
        for c in s:
            if c not in visited:
                visited.add(c)
            else:
                return c