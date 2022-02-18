class Solution:
    def maximum69Number (self, num: int) -> int:
        try:
            numstr = list(str(num))
            numstr[numstr.index('6')]='9'
            return int("".join(numstr))
        except:
            return num