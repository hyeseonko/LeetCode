import math
class Solution:
    def getSum(self, a: int, b: int) -> int:
        # math property: a^(a+b) = (a^a)*(a^b) --> a+b = log_a {(a^a)*(a^b)}
        return round(math.log2(pow(2,a)*pow(2,b)))