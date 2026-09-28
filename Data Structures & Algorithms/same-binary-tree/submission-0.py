# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p, q):
            if p is None or q is None:
                return p == q
            if p.val != q.val:
                return False

            pLeft, qLeft = p.left, q.left
            pRight, qRight = p.right, q.right

            if not dfs(pLeft, qLeft) or not dfs(pRight, qRight):
                return False
            return True

        
        return dfs(p, q)