# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0)
        cur = res
        carry = 0
        while l1 and l2:
            curVal = None
            if l1.val + l2.val + carry > 9:
                curVal = l1.val + l2.val + carry - 10
                carry = True
            else:
                curVal = l1.val + l2.val + carry
                carry = False
            cur.next = ListNode(curVal)
            cur = cur.next
            l1 = l1.next
            l2 = l2.next

        if l1:
            while l1:
                if l1.val + carry > 9:
                    curVal = l1.val + carry - 10
                    carry = True
                else:
                    curVal = l1.val + carry
                    carry = False
                cur.next = ListNode(curVal)
                cur = cur.next
                l1 = l1.next
        elif l2:
            while l2:
                if l2.val + carry > 9:
                    curVal = l2.val + carry - 10
                    carry = True
                else:
                    curVal = l2.val + carry
                    carry = False
                cur.next = ListNode(curVal)
                cur = cur.next
                l2 = l2.next
        if carry:
            cur.next = ListNode(1)
        return res.next