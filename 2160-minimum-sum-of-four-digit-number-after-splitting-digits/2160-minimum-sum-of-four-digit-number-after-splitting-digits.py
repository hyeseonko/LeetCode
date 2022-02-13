class Solution:
    def minimumSum(self, num: int) -> int:
        a = sorted([int(c) for c in str(num)])
        return a[0]*10+a[3]+a[1]*10+a[2]