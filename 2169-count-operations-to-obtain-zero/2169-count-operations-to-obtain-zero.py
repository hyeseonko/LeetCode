class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        count = 0
        small, big = (num1, num2) if num1<num2 else (num2, num1)
        while (small>0 and big>0):
            small, big = (small, big) if small<big else (big, small)
            big = big - small
            count+=1
        return count