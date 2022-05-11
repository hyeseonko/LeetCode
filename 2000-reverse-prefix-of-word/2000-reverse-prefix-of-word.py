class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        try:
            whereRU = word.index(ch)
            return word[:whereRU+1][::-1]+word[whereRU+1:]
        except:
            return word