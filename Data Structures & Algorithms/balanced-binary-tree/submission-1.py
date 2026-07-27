# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
                return (True, 0)

            (balancedLeft, heightLeft) = dfs(node.left)
            (balancedRight, heightRight) = dfs(node.right)
            height = max(heightLeft, heightRight) + 1
            if not (balancedLeft and balancedRight) or abs(heightRight - heightLeft) > 1:
                return (False, height)
            return (True, height)

        return dfs(root)[0]
