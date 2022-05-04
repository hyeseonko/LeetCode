# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode(0)
        head2 = head
        if head2:
            head2 = head2.next
        while(head):
            cur.next = ListNode(head.val)
            cur = cur.next
            if head.next:
                head = head.next.next
            else:
                break
        while(head2):
            cur.next = ListNode(head2.val)
            cur = cur.next
            if head2.next:
                head2 = head2.next.next
            else:
                break
        return dummy.next            
        