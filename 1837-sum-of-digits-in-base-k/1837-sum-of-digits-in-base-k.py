import math
class Solution:
    def sumBase(self, n: int, k: int) -> int:
        result=0
        max_seung=int(math.log(n, k))
        while(max_seung>=1):
            base = math.pow(k, max_seung)
            cur = n//base
            result+=cur
            max_seung-=1
            n-=(cur*base)
        result+=(n%k)
        return int(result)