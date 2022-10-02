class Solution:
    def partitionString(self, s: str) -> int:
        check=set()
        output=0
        for s1 in s:
            if s1 in check:
                check=set(s1)
                output+=1
            else:
                check.add(s1)
        return output+1