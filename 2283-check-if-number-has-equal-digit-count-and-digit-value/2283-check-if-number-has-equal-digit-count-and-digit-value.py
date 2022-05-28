class Solution:
    def digitCount(self, num: str) -> bool:
        for i, n in enumerate(num):
            if num.count(str(i))!=int(n):
                return False
        return True