class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        output=1
        bunmo=1
        for i, bunja in enumerate(range(m+n-2, max(m-1,n-1),-1)):
            output*=bunja
            bunmo*=(i+1)
        return int(output/bunmo)