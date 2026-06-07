# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        def bfs(node):
            q = deque()
            q.append(node)

            
            while q:
                level = []
                for i in range(len(q)):
                    curNode = q.popleft()
                    if curNode:
                        level.append(curNode.val)
                        directions = [curNode.left, curNode.right]
                        for dir in directions:
                            q.append(dir)
                if level:
                    res.append(level)
        bfs(root)
        return res
