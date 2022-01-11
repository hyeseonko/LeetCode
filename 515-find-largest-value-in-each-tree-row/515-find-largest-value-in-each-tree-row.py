# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        output = []
        stack=[(root, 0)]
        prev_level = 0
        cur_pool=[]
        while(stack):
            cur, cur_level = stack.pop(0)
            if cur_level!=prev_level:
                output.append(max(cur_pool))
                cur_pool.clear()
            cur_pool.append(cur.val)
            if cur.left:
                stack.append((cur.left, cur_level+1))
            if cur.right:
                stack.append((cur.right, cur_level+1))
            prev_level=cur_level
        output.append(max(cur_pool))
        return output