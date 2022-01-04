# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        candidates = []
        stack=[root]
        while(stack):
            cur = stack.pop(0)
            candidates.append(cur.val)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        sorted_candidates = sorted(candidates)
        for i, cand in enumerate(sorted_candidates):
            try:
                d = sorted_candidates[i+1:].index(k-cand)
                return True
            except:
                continue
        return False

# [1]
# 2