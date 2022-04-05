# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        len_node = 0
        cur = head
        while(cur):
            len_node+=1
            cur = cur.next
        len_cur = 0
        while(head):
            if len_cur == len_node//2:
                return head
            head = head.next
            len_cur +=1