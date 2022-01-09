# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # both does not exist
        if not root.left and not root.right:
            return True
        # one exists - left or right
        elif not root.left or not root.right:
            return False
        # both left and right exists
        stack1=[root.left]
        output1=[root.left.val]
        stack2=[root.right]
        output2=[root.right.val]
        # append left first
        while(stack1):
            cur = stack1.pop(0)
            if cur.left:
                stack1.append(cur.left)
                output1.append(cur.left.val)
            else:
                output1.append(101) # 101 = null
            if cur.right:
                stack1.append(cur.right)
                output1.append(cur.right.val)
            else:
                output1.append(101)
        # append right first
        while(stack2):
            cur = stack2.pop(0)
            if cur.right:
                output2.append(cur.right.val)
                stack2.append(cur.right)
            else:
                output2.append(101)
            if cur.left:
                output2.append(cur.left.val)
                stack2.append(cur.left)
            else:
                output2.append(101)

        if output1==output2:
            return True
        else:
            return False
        