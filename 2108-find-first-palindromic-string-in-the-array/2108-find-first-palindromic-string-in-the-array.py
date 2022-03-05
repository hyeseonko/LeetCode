class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            rev = word[::-1]
            if word == word[::-1]:
                return word
        return ""