# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:


        def dfs(p,q):
            if not p and not q:
                return True
            
            if not p and q:
                return False
            if not q and  p:
                return False
            
            if p.val != q.val:
                return False

            left = dfs(p.left,q.right)
            right = dfs(p.right,q.left)
            return left and right
        
        return dfs(root, root)
        