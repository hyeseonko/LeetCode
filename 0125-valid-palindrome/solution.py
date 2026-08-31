class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_s = [c.lower() for c in s if c.isalnum()]
        half_len = len(filtered_s) // 2
        for i in range(half_len):
            if filtered_s[i] != filtered_s[-i - 1]:
                return False
        return True
