"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        stack=[(root, 1)]
        while(stack):
            cur, level = stack.pop(0)
            if cur.children:
                for c in cur.children:
                    stack.append((c, level+1))
        return level