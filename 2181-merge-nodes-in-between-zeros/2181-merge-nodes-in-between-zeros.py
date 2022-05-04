# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode(0)
        flush = 0
        head = head.next
        while(head):
            if head.val==0:
                cur.next = ListNode(flush)
                cur = cur.next
                flush = 0
            else:
                flush+=head.val
            head = head.next
        return dummy.next