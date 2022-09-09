# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        q = [(root, 0)]
        output = 0
        while q:
            cur, where = q.pop(0)
            if not cur.left and not cur.right and where==-1:
                output+=cur.val
            if cur.left:
                q.append((cur.left, -1))
            if cur.right:
                q.append((cur.right, 1))
        return output