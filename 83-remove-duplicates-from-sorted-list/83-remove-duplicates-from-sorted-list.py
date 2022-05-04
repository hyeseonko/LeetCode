# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode(0)
        prev_val = -101
        while(head):
            if head.val!=prev_val:
                cur.next = ListNode(head.val)
                cur = cur.next
            prev_val = head.val
            head = head.next
        return dummy.next