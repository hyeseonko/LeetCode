# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        stack=[(root, 1)]
        output=0
        while(stack):
            node, where = stack.pop(0)
            if where==0 and not node.left and not node.right:
                output+=node.val
            if node.left:
                stack.append((node.left, 0))
            if node.right:
                stack.append((node.right, 1))
        return output
        