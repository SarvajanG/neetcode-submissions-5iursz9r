# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        final = []
        def dfs(root, d):
            if not root:
                return
            if len(res) == d:
                res.append([])
            res[d].append(root.val)
            dfs(root.left, d + 1)
            dfs(root.right, d + 1)
        dfs(root, 0)

        for l in res:
            final.append(l.pop())
        return final