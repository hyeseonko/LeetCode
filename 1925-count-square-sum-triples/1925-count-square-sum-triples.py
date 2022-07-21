import math
class Solution:
    def countTriples(self, n: int) -> int:
        total = 0
        for c in range(n, 0, -1):
            for b in range(c-1, 0, -1):
                a = math.sqrt(c**2-b**2)
                if a.is_integer():
                    total +=1
        return total