class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_s = [each for each in s if each.isalnum()]
        half_len = len(filtered_s)//2
        for i in range(half_len):
            if filtered_s[i].lower()!=filtered_s[-i-1].lower():
                return False
        return True

