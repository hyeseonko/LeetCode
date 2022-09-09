# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        output = 0
        if not root: return 0
        q = [(root, 1)]
        while q:
            cur, level = q.pop(0)
            if cur.left:
                q.append((cur.left, level+1))
            if cur.right:
                q.append((cur.right, level+1))
            output = level
        return output
            