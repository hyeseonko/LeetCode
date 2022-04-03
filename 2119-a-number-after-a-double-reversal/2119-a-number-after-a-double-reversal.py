class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return False if num>0 and str(num)[-1]=="0" else True
            