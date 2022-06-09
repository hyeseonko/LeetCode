class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        num = re.findall(r'\d+', s)
        prev = int(num[0])
        for n in num[1:]:
            cur = int(n)
            if prev>=cur:
                return False
            prev = cur
        return True
