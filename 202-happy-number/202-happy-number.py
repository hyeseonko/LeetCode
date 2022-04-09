class Solution:
    def isHappy(self, n: int) -> bool:
        pool = set()
        pool.add(n)
        result=n
        while(result>1):
            strn = str(result)
            result = 0
            for c in strn:
                result+=int(c)*int(c)
            if result in pool:
                return False
            pool.add(result)
        return True