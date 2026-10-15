"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur = head
        oldToNew = {}
        dummy = Node(0)
        res = dummy
        while cur:
            oldToNew[cur] = Node(cur.val, None, None)
            cur = cur.next
        
        cur = head
        while cur:
            newNode = oldToNew[cur]
            res.next = newNode
            if cur.random:
                newNode.random = oldToNew[cur.random]
            res = res.next
            cur = cur.next
        return dummy.next