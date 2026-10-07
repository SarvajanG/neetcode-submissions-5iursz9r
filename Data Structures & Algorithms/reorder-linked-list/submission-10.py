# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        cur, nxt, prev = slow, None, None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        first, second = head, prev
        firstNxt, secondNxt = None, None
        while second.next:
            firstNxt = first.next
            secondNxt = second.next
            first.next = second
            second.next = firstNxt
            first = firstNxt
            second = secondNxt
