# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        stack=[(root, 0)]
        output=[]
        same_depth=[]
        cur_depth=0

        while(stack):
            cur, depth = stack.pop(0)
            if depth==cur_depth:
                same_depth.append(cur.val)
            else:
                output.append(same_depth)
                same_depth=[cur.val]
                cur_depth+=1

            if cur.left:
                stack.append((cur.left, depth+1))
            if cur.right:
                stack.append((cur.right, depth+1))
        
        output.append(same_depth)

        return output
            