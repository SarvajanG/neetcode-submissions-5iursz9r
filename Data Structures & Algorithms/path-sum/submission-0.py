# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, currentSum):
            if not root:
                return
            currentSum += root.val
            if currentSum == targetSum and root.left == None and root.right == None:
                return True
            return dfs(root.left, currentSum) or dfs(root.right, currentSum)
        return True if dfs(root, 0) else False
