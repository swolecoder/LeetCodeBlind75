# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = float('-inf')
        def dfs(node):
            nonlocal ans
            if not node:
                # diameterr and height
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            d = left + right 
            ans = max(d, ans)
            return max(left, right) + 1
        dfs(root)
        return ans 
        