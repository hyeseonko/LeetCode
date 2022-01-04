# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        bottomleft=root.val
        stack=[(root, 0)]
        prev_depth=0
        while(stack):
            cur, depth = stack.pop(0)
            if depth!=prev_depth:
                bottomleft=cur.val
            if cur.left:
                stack.append((cur.left, depth+1))
            if cur.right:
                stack.append((cur.right, depth+1))
            prev_depth=depth
        return bottomleft