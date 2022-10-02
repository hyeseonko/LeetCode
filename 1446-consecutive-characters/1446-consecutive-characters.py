class Solution:
    def maxPower(self, s: str) -> int:
        prev=None
        output = 0
        result = 0
        for s1 in s:
            if prev is not None and prev!=s1:
                output = 0
            prev = s1
            output+=1
            if result<output:
                result=output
        return result