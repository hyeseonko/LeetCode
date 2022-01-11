# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0  # root
        stack=[(root, root.val)]
        while(stack):
            
            cur, from_value = stack.pop(0)
            if cur.val >= from_value:
                result+=1
                to_value = cur.val
            else:
                to_value = from_value
            if cur.left:
                stack.append((cur.left, to_value))
            if cur.right:
                stack.append((cur.right, to_value))
        
        return result