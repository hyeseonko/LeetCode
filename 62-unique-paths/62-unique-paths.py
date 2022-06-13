class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Combinatorics: (m-1)+(n-1) C min(m-1,n-1)
        output=1
        bunmo=1
        for i, bunja in enumerate(range(m+n-2, max(m,n)-1,-1), 1):
            output*=bunja
            bunmo*=i
        return output//bunmo