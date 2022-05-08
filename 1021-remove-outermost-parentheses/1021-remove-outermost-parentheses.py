class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        # (=1, )=-1
        makingZeroIndices=[0,]
        param=1
        for i, each in enumerate(s[1:-1], 1):
            param+=1 if each=="(" else -1
            if param==0:
                makingZeroIndices.extend([i, i+1])
        for index in makingZeroIndices[::-1]:
            s=s[:index]+s[index+1:]
        return s[:-1]
            
            