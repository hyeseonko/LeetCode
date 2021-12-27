# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        output=[]
        stack=[(root,0)]
        prev_depth=0
        while(stack):
            node, depth = stack.pop(0)
            if depth!=prev_depth:
                output.append(prev_node.val)
            if node.left:
                stack.append((node.left, depth+1))
            if node.right:
                stack.append((node.right, depth+1))
            prev_depth=depth
            prev_node=node
        output.append(prev_node.val)
        return output
        