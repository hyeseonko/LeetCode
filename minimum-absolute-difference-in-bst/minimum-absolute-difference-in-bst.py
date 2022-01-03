# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        output =[]
        stack=[root]
        while(stack):
            cur = stack.pop(0)
            output.append(cur.val)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        output = sorted(output)
        min_diff = 100000
        for i in range(len(output)-1):
            cand = output[i+1]-output[i]
            if cand < min_diff:
                min_diff = cand
        return min_diff