# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(p,q):
            if not p and q:
                return False
            if p and not q:
                return False
            if not p and not q:
                return True
            if p.val != q.val:
                return False
            
            left = sameTree(p.left, q.left)
            right = sameTree(p.right, q.right)
            return left and right
        
        if root and not subRoot:
            return True
        if not root and subRoot:
            return False
        if sameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        