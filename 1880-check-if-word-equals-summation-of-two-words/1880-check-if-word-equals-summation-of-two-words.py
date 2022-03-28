import string
import math
class Solution:
    di = {c: n for c, n in zip(string.ascii_lowercase, range(26))}
    def word2num(self, word):
        num=0
        for i, word in enumerate(word[::-1]):
            num+=self.di[word]*math.pow(10, i)
        return num
        
        
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        return True if self.word2num(firstWord)+self.word2num(secondWord)==self.word2num(targetWord) else False

        