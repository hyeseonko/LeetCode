class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # solution 1. dp
        # solution 2. math : (m+n-2)C(min(m-1,n-1))
        output=1
        bunmo=1
        for i, bunja in enumerate(range(m+n-2, max(m-1,n-1),-1)):
            output*=bunja
            bunmo*=(i+1)
        return int(output/bunmo)
        
        
        