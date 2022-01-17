class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        dp=[s[-i] for i in range(1,len(s)+1)]
        for each in t:
            if len(dp)>0 and each==dp[-1]:
                dp.pop()
        if len(dp)==0:
            return True
        else:
            return False