# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        queue=[root]
        result=0
        while(queue):
            cur = queue.pop(0)
            if cur.val in range(low, high+1):
                result+=cur.val
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        return result