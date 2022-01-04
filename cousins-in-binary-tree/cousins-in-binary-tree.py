# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        # condition to be cousin: (1) diff.parents (2) same level
        stack=[(root, 0, -1)]
        xlevel, ylevel = -1, -1
        xparent, yparent = -1, -1
        while(stack):
            cur, depth, parent = stack.pop(0)
            if cur.val==x:
                xlevel, xparent = depth, parent
            if cur.val==y:
                ylevel, yparent = depth, parent
            if cur.left:
                stack.append((cur.left, depth+1, cur.val))
            if cur.right:
                stack.append((cur.right, depth+1, cur.val))
        if xlevel==ylevel and xparent!=yparent:
            return True
        else:
            return False