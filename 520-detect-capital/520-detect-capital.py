class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        start=False
        if word[0].isupper():
            start=True
        
        if len(word)<2: return True
        middle=False
        if word[1].isupper():
            middle=True
        for w in word[1:]:
            if start:
                # ALL UPPER
                if middle:
                    if w.islower():
                        return False
                # ALL LOWER
                else:
                    if w.isupper():
                        return False
            else:
                if w.isupper():
                    return False
        return True