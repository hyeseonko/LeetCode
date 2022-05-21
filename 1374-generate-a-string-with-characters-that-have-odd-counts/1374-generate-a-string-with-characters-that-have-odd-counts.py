class Solution:
    def generateTheString(self, n: int) -> str:
        return "a"+"b"*(n-1) if n==1 or n%2==0 else "ab"+"c"*(n-2)