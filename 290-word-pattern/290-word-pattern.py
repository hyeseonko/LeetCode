class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(pattern)!=len(s.split(" ")):
            return False
        di = dict()
        wordset = set()
        for p, word in zip(pattern, s.split(" ")):
            if p not in di:
                if word not in wordset:
                    di[p]=word
                    wordset.add(word)
                else:
                    return False
            elif di[p]!=word:
                return False
        return True