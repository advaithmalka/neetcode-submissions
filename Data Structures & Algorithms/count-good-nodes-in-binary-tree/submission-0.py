# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(node, maxNode):
            if not node:
                return

            nonlocal res
            if node.val >= maxNode:
                res += 1
                maxNode = node.val

            dfs(node.left, maxNode)
            dfs(node.right, maxNode)
        
        dfs(root, root.val)
        return res