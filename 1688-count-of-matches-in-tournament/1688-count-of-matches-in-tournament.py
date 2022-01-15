class Solution:
    def numberOfMatches(self, n: int) -> int:
        result=0
        while(n>1):
            k=int(n/2)
            result+=k
            n-=k
        return result
        