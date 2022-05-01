class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s2 = ""
        t2 = ""
        for each in s:
            if each=="#":
                s2 = s2[:-1]
            else:
                s2+=each
        for each in t:
            if each=="#":
                t2 = t2[:-1]
            else:
                t2+=each
        
        return s2==t2
        