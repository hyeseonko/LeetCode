# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        all_leaves=[]
        cur_leaves = []
        stack=[(root,0)]
        prev_level=0
        while(stack):
            cur, level = stack.pop(0)
            if prev_level!=level:
                all_leaves.append(cur_leaves)
                cur_leaves.clear()
            cur_leaves.append(cur.val)
            if cur.left:
                stack.append((cur.left, level+1))
            if cur.right:
                stack.append((cur.right, level+1))
            prev_level = level
        all_leaves.append(cur_leaves)
        return sum(all_leaves[-1])