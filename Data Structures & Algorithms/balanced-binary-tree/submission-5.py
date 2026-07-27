# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, height):
            if not node:
                return height

            leftHeight = dfs(node.left, height + 1)
            if leftHeight == -1: 
                return -1

            rightHeight = dfs(node.right, height + 1)
            if rightHeight == -1: 
                return -1

            if abs(leftHeight - rightHeight) > 1:
                return -1

            return max(leftHeight, rightHeight)

        return dfs(root, 1) != -1