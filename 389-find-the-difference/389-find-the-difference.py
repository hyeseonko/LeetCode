class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        t_dict=dict()
        for each in t:
            if each not in t_dict:
                t_dict[each]=0
            t_dict[each]+=1
        for c in t_dict:
            if s.count(c)!=t_dict[c]:
                return c