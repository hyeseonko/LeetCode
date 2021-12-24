# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif (p and not q) or (not p and q):
            return False
        else:
            stack=[(p, q)]
            while(stack):
                cur_p, cur_q = stack.pop(0)
                if cur_p.val!=cur_q.val:
                    return False
                if cur_p.left and cur_q.left:
                    stack.append((cur_p.left, cur_q.left))
                if cur_p.right and cur_q.right:
                    stack.append((cur_p.right, cur_q.right))
                if (cur_p.left and not cur_q.left) or (not cur_p.left and cur_q.left):
                    return False
                if (cur_p.right and not cur_q.right) or (not cur_p.right and cur_q.right):
                    return False
            return True