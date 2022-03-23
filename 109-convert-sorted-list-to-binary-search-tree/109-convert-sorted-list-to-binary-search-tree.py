# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        slist=[]
        while(head):
            slist.append(head.val)
            head = head.next
        def recursiveBST(low, high):
            if low>high:
                return None
            mid = (low+high)//2
            return TreeNode(slist[mid], recursiveBST(low, mid-1), recursiveBST(mid+1, high))
        return recursiveBST(0, len(slist)-1)