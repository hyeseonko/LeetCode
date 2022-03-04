class Solution:
    def isPalindrome(self, s: str) -> bool:
        org = re.sub(r'[^a-z0-9]+', '', s.lower())
        rev = org[::-1]
        return True if org==rev else False