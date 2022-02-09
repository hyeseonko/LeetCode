class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s_dict=dict()
        for each in s:
            if each not in s_dict:
                s_dict[each]=0
            s_dict[each]+=1
        for k, v in s_dict.items():
            if t.count(k)!=v:
                return False
        return True