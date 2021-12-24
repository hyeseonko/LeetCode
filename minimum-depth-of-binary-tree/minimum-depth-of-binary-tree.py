# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack=[(root, 1)]
        while(stack):
            cur, cur_depth = stack.pop(0)
            if not cur.left and not cur.right:
                return cur_depth
            if cur.left:
                stack.append((cur.left, cur_depth+1))
            if cur.right:
                stack.append((cur.right, cur_depth+1))
        return cur_depth
                
            
        