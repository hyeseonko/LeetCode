class Solution:
    def generateParenthesis(self, n):
        # method 1. stack
        output = []
        stack=[("(", 1, 0)]
        while stack:
            cur, l, r = stack.pop(0)
            if l < r or l>n or r>n:
                continue
            if l==n and r==n:
                output.append(cur)
            stack.append((cur+"(", l+1, r))
            stack.append((cur+")", l, r+1))
        return output   