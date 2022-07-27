from itertools import zip_longest

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        temp = 0
        output = ''
        for a1, b1 in zip_longest(a[::-1], b[::-1], fillvalue=0):
            num = int(a1)+int(b1)+temp
            output+=str(num%2)
            temp = num//2
        output+=str(temp) if temp==1 else ''
        return output[::-1]