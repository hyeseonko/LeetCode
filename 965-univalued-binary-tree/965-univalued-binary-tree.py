# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        univalue=root.val
        stack=[root]
        while(stack):
            cur = stack.pop(0)
            if cur.val!=univalue:
                return False
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return True  