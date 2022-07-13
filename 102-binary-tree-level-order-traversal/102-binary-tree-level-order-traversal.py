# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        if not root:
            return output
        queue = [(root, 0)] # node, level
        prev = 0
        temp = []
        while queue:
            cur, level = queue.pop(0)
            
            if level!=prev:
                output.append(temp)
                temp=[cur.val]
            else:
                temp.append(cur.val)
            
            if cur.left:
                queue.append((cur.left, level+1))
            if cur.right:
                queue.append((cur.right, level+1))
                
            prev = level
        
        output.append(temp)
        return output