class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        return sum([1 for word in words if word==s[:len(word)]])