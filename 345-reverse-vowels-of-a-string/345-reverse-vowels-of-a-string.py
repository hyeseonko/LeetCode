class Solution:
    def reverseVowels(self, s: str) -> str:
        # leetcode 
        # 1:e, 2:e, 5:o,7:e
        vowels=""
        for s1 in s[::-1]:
            if s1 in {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}:
                vowels+=s1
        result=""
        idx=0
        for i in range(len(s)):
            if s[i] in {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}:
                result+=vowels[idx]
                idx+=1
            else:
                result+=s[i]
        return result