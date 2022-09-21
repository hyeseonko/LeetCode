class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for n in range(num+1):
            if n*n==num:
                return True
            elif n*n>num:
                return False
            else:
                continue
        