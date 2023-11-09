# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def helper(node, l,r):
            if not node:
                return True
            
            if not (node.val > l and node.val < r):
                return False
            
            return helper(node.left, l , node.val) and helper(node.right, node.val , r)
        
        return helper(root, float("-inf"), float("inf"))

        