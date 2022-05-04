# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = cur = ListNode(0)
        while(head):
            if head.val != val:
                cur.next = ListNode(head.val)
                cur = cur.next
            head = head.next
        return dummy.next