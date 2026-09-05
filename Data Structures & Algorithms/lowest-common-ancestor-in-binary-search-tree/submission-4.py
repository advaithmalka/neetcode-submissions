# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root
        while not (p.val <= curr.val <= q.val or q.val <= curr.val <= p.val):
            if curr.val < p.val and curr.val < q.val:
                curr = curr.right
            else:
                curr = curr.left
        return curr