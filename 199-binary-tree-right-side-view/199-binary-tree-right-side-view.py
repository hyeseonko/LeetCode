# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # method 1. BFS
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output, queue = [], []
        if not root:
            return output
        
        queue = [(root, 0)] # node, level
        val = root.val
        prev_level = 0
        while queue:
            cur, cur_level = queue.pop(0)
            if cur_level!=prev_level:
                output.append(val)
            if cur.left:
                queue.append((cur.left, cur_level+1))
            if cur.right:
                queue.append((cur.right, cur_level+1))
            prev_level = cur_level
            val = cur.val
        output.append(val)
        return output