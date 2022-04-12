class Solution:
    def balancedStringSplit(self, s: str) -> int:
        # R: +1, L: -1
        output = 0
        cur = 0
        for step in s:
            if step=="R":
                cur+=1
            else:
                cur-=1
            if cur==0:
                output+=1
        return output