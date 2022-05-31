import math
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        return 2**k==len({s[i:i+k] for i in range(len(s)-k+1)})
            