# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        queue=[(root, root.val)]
        while(queue):
            cur, val = queue.pop(0)
            if not cur.left and not cur.right and val == targetSum:
                return True
            if cur.left:
                queue.append((cur.left, val+cur.left.val))
            if cur.right:
                queue.append((cur.right, val+cur.right.val))
        return False