# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        stack=[(root,0)]
        prev_level = 0
        same_level = [root.val]
        output = []
        while(stack):
            cur, level = stack.pop(0)
            if level!=prev_level:
                output.append(sum(same_level))
                same_level.clear()
            same_level.append(cur.val)
            if cur.left:
                stack.append((cur.left, level+1))
            if cur.right:
                stack.append((cur.right, level+1))
            prev_level = level
        output.append(sum(same_level))
        return output.index(max(output))+1