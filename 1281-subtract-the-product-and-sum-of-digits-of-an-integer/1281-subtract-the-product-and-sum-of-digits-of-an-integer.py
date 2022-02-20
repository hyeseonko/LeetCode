class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        _product=1
        _sum=0
        for c in str(n):
            _product*=int(c)
            _sum+=int(c)
        return _product-_sum