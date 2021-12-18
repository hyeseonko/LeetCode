class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1:
            return strs[0]
        minlen = min([len(each) for each in strs])
        result=""
        for i in range(minlen):
            basis = strs[-1][i]
            for j in range(len(strs)-1):
                if basis!=strs[j][i]:
                    return result
            result+=basis
        return result
        
        # case: long common string (not prefix)
        # result=""
        # for s1 in strs[0]:
        #     nolook=False
        #     for s2 in strs[1:]:
        #         if result+s1 not in s2:
        #             nolook=True
        #             break
        #     print(s1, s2, result, nolook)
        #     if nolook==False:
        #         result+=s1
        # return result