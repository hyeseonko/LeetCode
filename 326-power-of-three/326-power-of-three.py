class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return str(round(math.log(n, 3), 10)).split(".")[-1]=='0' if n>0 else False