# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodNodes = 0
        def dfs(root, largest):
            if not root:
                return
            nonlocal goodNodes
            if root.val >= largest:
                goodNodes += 1
                largest = root.val
            dfs(root.left, largest)
            dfs(root.right, largest)
        dfs(root, root.val)
        return goodNodes