class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        output = 0
        stack=["("]
        for each in s[1:]:
            if each=="(":
                stack.append("(")
            else:
                if stack[-1]=="(":
                    stack.pop(-1)
                    stack.append(1)
                else:
                    current = 0
                    while(1):
                        if stack[-1]=="(":
                            stack.pop(-1)
                            stack.append(2*current)
                            break
                        current+=stack.pop(-1)
        return sum(stack)