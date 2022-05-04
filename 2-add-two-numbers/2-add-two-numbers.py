# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode(0) # dummy = static, cur = dynamic 
        remainder = 0
        while(l1 or l2 or remainder):
            if l1:
                remainder+=l1.val
                l1 = l1.next
            if l2:
                remainder+=l2.val
                l2 = l2.next
            cur.next=ListNode(remainder%10)
            cur = cur.next
            remainder//=10
        return dummy.next