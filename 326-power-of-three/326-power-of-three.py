class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # log
        # return str(round(math.log(n, 3), 10)).split(".")[-1]=='0' if n>0 else False
        
        # number theory
        return n>0 and not 3**19 % n