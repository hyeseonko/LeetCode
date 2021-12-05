class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        valid={"}": "{", ")":"(", "]":"["}
        for each in s:
            if each in {")", "}", "]"}:
                if len(stack)>0 and stack[-1]==valid[each]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(each)

        if len(stack)==0:
            return True
        else:
            return False