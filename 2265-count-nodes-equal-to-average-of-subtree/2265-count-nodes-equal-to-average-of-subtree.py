# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Reference
# Inspired by this solution: https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/discuss/2018060/Python-or-DFS-or-Easy-to-Understand

class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        result = 0
        
        def dfs(node):
            nonlocal result
            if not node:
                return 0, 0 # sum, count
            
            l_sum, l_cnt = dfs(node.left)
            r_sum, r_cnt = dfs(node.right)
            c_sum = node.val+l_sum+r_sum # current_sum
            c_cnt = 1+l_cnt+r_cnt # current_count
            if c_sum//c_cnt==node.val:
                result+=1
            return c_sum, c_cnt
            
        dfs(root)
        return result