import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        org = re.sub(r'[^a-z0-9]+', '', s.lower())
        return org == org[::-1]
