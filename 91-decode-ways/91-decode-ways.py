class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0]=="0":
            return 0
        dp=[1, 1]
        prev=s[0]
        for each in s[1:]:
            result=0
            if each!="0":
                result+=dp[-1]
            if prev!="0" and int(prev+each)<=26 and int(prev+each)>=1:
                result+=dp[-2]
            dp.append(result)
            prev=each
        return dp[-1]