import math
class Solution:
    def countEven(self, num: int) -> int:
        output = 0
        for n in range(1, num+1):
            total = 0
            for each in str(n):
                total += int(each)
            if total%2==0:
                output+=1
        return output