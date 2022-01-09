# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        output=[]
        stack=[root]
        while(stack):
            cur = stack.pop(0)
            output.append(cur.val)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        sorted_output=sorted(output)
        diff = sorted_output[1]-sorted_output[0]
        for i in range(2,len(sorted_output)):
            if sorted_output[i]-sorted_output[i-1]<diff:
                diff=sorted_output[i]-sorted_output[i-1]
        return diff