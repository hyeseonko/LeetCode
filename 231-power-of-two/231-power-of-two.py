import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n and not (n & n - 1) # n <- added because of 0

        # if n<=0:
        #     return False
        # if str(math.log2(n)).split(".")[-1]=="0":
        #     return True
        # else:
        #     return False