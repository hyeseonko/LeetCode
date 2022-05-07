# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        output=[]
        digit2alphabet = dict((i, key) for i, key in enumerate(string.ascii_lowercase))
        queue=[(root, digit2alphabet[root.val])]
        while(queue):
            cur, curstr = queue.pop(0)
            if cur.left:
                queue.append((cur.left, digit2alphabet[cur.left.val]+curstr))
            if cur.right:
                queue.append((cur.right, digit2alphabet[cur.right.val]+curstr))
            if not cur.left and not cur.right:
                output.append(curstr)
        return sorted(output)[0]