class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        t_list=[each for each in t]
        for each in s:
            if each in t_list:
                t_list.remove(each)
        return t_list[0]
        