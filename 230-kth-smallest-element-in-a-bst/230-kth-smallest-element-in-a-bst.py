# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        output = []
        queue=[root]
        while(queue):
            cur = queue.pop(0)
            output.append(cur.val)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        sorted_output = sorted(output)[k-1]
        return sorted_output