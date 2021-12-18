class Solution:
    def longestPalindrome(self, s: str) -> int:
        str_dict={}
        for each in s:
            if each not in str_dict:
                str_dict[each]=0
            str_dict[each]+=1
        result=0
        odd=0
        for k, v in str_dict.items():
            if v%2==0:
                result+=v
            else:
                result+=v-1
                odd=1
        return result+odd