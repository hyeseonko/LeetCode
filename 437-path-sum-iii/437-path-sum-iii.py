# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        output=0
        queue=[(root, [root.val])]
        while(queue):
            cur, val_list = queue.pop(0)
            for idx in range(len(val_list)):
                if sum(val_list[idx:])==targetSum:
                    output+=1
            if cur.left:
                queue.append((cur.left, val_list+[cur.left.val]))
            if cur.right:
                queue.append((cur.right, val_list+[cur.right.val]))
        return output