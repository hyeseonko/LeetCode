class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        if a<b:
            _min, _max = a, b
        else:
            _min, _max = b, a

        result = 1
        diff = _max - _min
        gcd = _min
        while(diff):
            diff = _max-_min
            if a%diff==0 and b%diff==0:
                gcd = diff
                break
            if _min<diff:
                _min, _max = _min, diff
            else:
                _min, _max = diff, _min

        for i in range(2, gcd+1):
            if a%i==0 and b%i==0:
                result+=1
        return result