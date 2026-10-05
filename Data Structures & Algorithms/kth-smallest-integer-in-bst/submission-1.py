# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        num = 0
        res = root.val
        def dfs(node):
            if not node: 
                return 

            nonlocal num, res
            dfs(node.left)
            num += 1
            if num == k:
                res = node.val
                return
            dfs(node.right)
        dfs(root)
        return res
                
