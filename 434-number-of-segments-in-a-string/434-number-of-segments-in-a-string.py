class Solution:
    def countSegments(self, s: str) -> int:
        return sum([1 for letter in s.strip().split(" ") if letter])