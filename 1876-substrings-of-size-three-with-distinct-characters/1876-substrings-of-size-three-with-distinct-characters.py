class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        output = 0
        for i in range(len(s)-2):
            if len(set(s[i:i+3]))==3:
                output+=1
        return output