# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def dfs(p,q):
            if not p and not q:
                return True
            if p and not q:
                return False
            if not p and q:
                return False
            if p.val != q.val:
                return False
            left = dfs(p.left, q.left)
            right = dfs(p.right, q.right)
            return left and right
        
        if dfs(root, subRoot):
            return True
        if root and not subRoot:
            return False
        if not root and subRoot:
            return False
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)
        return left or right
        