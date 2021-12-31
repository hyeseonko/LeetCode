# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        output=[]
        stack = [(root, 0)]
        same_level=[]
        prev_level = 0
        while(stack):
            cur, level = stack.pop(0)

            if level!=prev_level:
                same_num = len(same_level)
                same_sum = sum(same_level)
                same_level.clear()
                output.append(same_sum/same_num)
                same_level.append(cur.val)
            else:
                same_level.append(cur.val)
            
            if cur.left:
                stack.append((cur.left, level+1))
            if cur.right:
                stack.append((cur.right, level+1))
                
            prev_level=level
        same_num = len(same_level)
        same_sum = sum(same_level)
        output.append(same_sum/same_num)
        return output
            