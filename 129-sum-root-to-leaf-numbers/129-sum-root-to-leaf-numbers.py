# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        queue=[(root, root.val)]
        output=0
        while(queue):
            cur, digit = queue.pop(0)
            if cur.left:
                queue.append((cur.left, digit*10+cur.left.val))
            if cur.right:
                queue.append((cur.right, digit*10+cur.right.val))
            if not cur.left and not cur.right:
                output+=digit
        return output