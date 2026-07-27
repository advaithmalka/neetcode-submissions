# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, h):
            if not node:
                return (h, True) 

            leftH, balancedLeft = dfs(node.left, h + 1)
            rightH, balancedRight = dfs(node.right, h + 1)
            if not (balancedLeft and balancedRight) or abs(leftH - rightH) > 1:
                return (h, False)
                
            return (max(leftH, rightH), True)
        return dfs(root, 1)[1]