# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        


        def helper(node, val):
            if not node:
                return True
            
            if node.val != val:
                return False
            
            return helper(node.left,val) and helper(node.right,val)
        
        return helper(root,root.val)
        