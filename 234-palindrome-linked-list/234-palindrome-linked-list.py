# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        palin = []
        while(head):
            palin.append(head.val)
            head = head.next
        return palin==palin[::-1]