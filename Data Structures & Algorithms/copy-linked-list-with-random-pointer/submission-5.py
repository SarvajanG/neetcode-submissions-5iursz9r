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
        dummy = Node(0)
        cur2 = dummy
        valToNode = {}
        while cur:
            valToNode[cur] = Node(cur.val, None, None)
            cur = cur.next

        cur = head
        while cur:
            curNode = valToNode[cur]
            if cur.random:
                curNode.random = valToNode[cur.random]
            cur2.next = curNode
            cur2 = cur2.next
            cur = cur.next

        return dummy.next
        

        