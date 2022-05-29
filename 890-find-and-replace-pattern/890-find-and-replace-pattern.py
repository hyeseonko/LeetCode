class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        # Brute-force
        output = []
        pattern_matching = []
        for p in set(pattern):
            pattern_matching.append([x for x, e in enumerate(pattern) if e==p])
        pattern_matching.sort()
        for word in words:
            current_matching = []
            for c in set(word):
                current_matching.append([x for x, e in enumerate(word) if e==c])
            current_matching.sort()
            if current_matching==pattern_matching:
                output.append(word)
        return output