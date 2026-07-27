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
                return (0, True) 

            leftH, balancedLeft = dfs(node.left)
            if not balancedLeft: return (-1, False)
            rightH, balancedRight = dfs(node.right)
            if not balancedRight: return (-1, False)
            if not (balancedLeft and balancedRight) or abs(leftH - rightH) > 1:
                return (-1, False)
                
            return (max(leftH, rightH) + 1, True)
        return dfs(root)[1]