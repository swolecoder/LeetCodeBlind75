# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return 
        
        def dfs(node):
            if not node:
                return 
            
            if node.val == val:
                print("hellp")
                return node
            left = dfs(node.left)
            if left:
                return left
            right = dfs(node.right)
            if right:
                return right
        return dfs(root)