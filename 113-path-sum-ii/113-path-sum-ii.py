# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        output=[]
        queue = [(root, [root.val])]
        while(queue):
            cur, val_list = queue.pop(0)
            if not cur.left and not cur.right and sum(val_list)==targetSum:
                output.append(val_list)
            if cur.left:
                queue.append((cur.left, val_list+[cur.left.val]))
            if cur.right:
                queue.append((cur.right, val_list+[cur.right.val]))
        return output