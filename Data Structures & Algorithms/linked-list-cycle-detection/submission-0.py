# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur = head

        while cur:
            if cur.val == "Z":
                return True
            else:
                cur.val = "Z"
            cur = cur.next
        return False