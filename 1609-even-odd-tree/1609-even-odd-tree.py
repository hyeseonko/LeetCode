# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        stack=[(root, 0)]
        prev_level = 0
        cur_pool=[]
        while(stack):
            cur, level = stack.pop(0)
            if prev_level!=level:
                # cur_pool with prev_level(=level-1)
                prev_item=cur_pool[0]
                remainder=level%2
                if prev_item%2!=remainder:
                    return False
                for item in cur_pool[1:]:
                    if item%2!=remainder:
                        return False
                    if remainder==0 and prev_item<=item:
                        return False 
                    if remainder==1 and prev_item>=item:
                        return False
                    prev_item=item                                        
                cur_pool.clear()
            cur_pool.append(cur.val)
            prev_level=level
            if cur.left:
                stack.append((cur.left, level+1))
            if cur.right:
                stack.append((cur.right, level+1))
        # last row
        prev_item=cur_pool[0]
        remainder=(level+1)%2
        if prev_item%2!=remainder:
            return False
        for item in cur_pool[1:]:
            if item%2!=remainder:
                return False
            if remainder==0 and prev_item<=item:
                return False 
            if remainder==1 and prev_item>=item:
                return False
        return True