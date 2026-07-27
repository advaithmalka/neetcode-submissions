class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(l, h, node):
            if not node:
                return True
            if not (l < node.val < h):
                return False
            
            return dfs(l, node.val, node.left) and dfs(node.val, h, node.right)

        return dfs(-1001, 1001, root)