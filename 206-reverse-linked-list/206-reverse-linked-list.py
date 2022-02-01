# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail=None
        while(head):
            cur = ListNode(val = head.val, next=tail)
            tail = cur
            head = head.next
        return tail