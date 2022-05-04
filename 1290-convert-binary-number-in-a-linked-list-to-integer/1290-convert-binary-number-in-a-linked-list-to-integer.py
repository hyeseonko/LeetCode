# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        stack = []
        while(head):
            stack.append(head.val)
            head = head.next
        digit, output = 0, 0
        while(stack):
            num = stack.pop(-1)
            output += num*math.pow(2, digit)
            digit+=1
        return round(output)