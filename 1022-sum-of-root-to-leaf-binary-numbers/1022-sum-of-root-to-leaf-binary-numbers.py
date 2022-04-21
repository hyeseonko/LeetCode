# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        queue=[(root, "")]
        output = 0
        while(queue):
            cur, num = queue.pop(0)
            if cur.left:
                queue.append((cur.left, num+str(cur.val)))
            if cur.right:
                queue.append((cur.right, num+str(cur.val)))
            if not cur.left and not cur.right:
                output+=int(num+str(cur.val), 2)
        return output