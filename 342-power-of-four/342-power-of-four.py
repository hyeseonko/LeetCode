class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n>0 and str(round(math.log(n, 4), 10)).split(".")[-1]=="0"