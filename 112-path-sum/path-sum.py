# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(root, curr):
            if not root:
                return 
            
            curr += root.val
            if not root.left and not root.right and curr == targetSum:
                return True
            left = dfs(root.left, curr)
            right = dfs(root.right,curr)
            return left or right
        
        return dfs(root,0)
            

        