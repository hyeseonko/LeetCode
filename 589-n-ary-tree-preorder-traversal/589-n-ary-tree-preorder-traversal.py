"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root: return []
        stack=[root]
        output = []
        while stack:
            temp = stack.pop()
            output.append(temp.val)
            stack.extend(temp.children[::-1]) # in a reverse order
        return output