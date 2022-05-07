class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        longerword = word1 if len(word1)>len(word2) else word2
        restword = longerword[min(len(word1), len(word2)):]
        output=""
        for w1, w2 in zip(word1, word2):
            output+=w1
            output+=w2
        output+=restword
        return output