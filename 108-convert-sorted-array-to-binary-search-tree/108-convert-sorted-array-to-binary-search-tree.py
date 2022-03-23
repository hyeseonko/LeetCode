# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def recursiveBST(low, high):
            if low > high:
                return None
            mid = (low+high)//2
            return TreeNode(nums[mid], recursiveBST(low, mid-1), recursiveBST(mid+1, high))
        return recursiveBST(0, len(nums)-1)