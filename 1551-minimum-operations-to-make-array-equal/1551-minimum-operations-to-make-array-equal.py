class Solution:
    def minOperations(self, n: int) -> int:
        # return (n//2)**2 if n%2==0 else ((n+1)//2)**2-((n+1)//2)
        return n**2//4