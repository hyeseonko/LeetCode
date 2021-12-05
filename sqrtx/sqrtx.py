class Solution:
    def mySqrt(self, x: int) -> int:
        # solution 1. go thourgh all numbers
        # i=0
        # while(1):
        #     if x>=i*i and x<(i+1)*(i+1):
        #         return i
        #     i+=1
        # solution 2. sqrt
        return int(sqrt(x))
        
