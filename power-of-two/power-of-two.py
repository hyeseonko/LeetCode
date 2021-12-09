class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        
        import math
        if str(math.log2(n)).split(".")[-1]=="0":
            return True
        else:
            return False