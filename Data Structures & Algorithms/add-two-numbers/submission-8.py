# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        cur = res
        carry = 0
        while l1 or l2 or carry:
            curVal = 0
            if l1:
                curVal += l1.val
            if l2:
                curVal += l2.val
            curVal += carry
            carry = curVal//10
            curVal = curVal % 10
            cur.next = ListNode(curVal)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            cur = cur.next
        return res.next