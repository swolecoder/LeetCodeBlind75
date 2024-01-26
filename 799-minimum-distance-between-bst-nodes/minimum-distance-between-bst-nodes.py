# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:

        ans = float('inf')
        prev = None

        def dfs(node):
            nonlocal ans, prev
            if not node:
                return 
            dfs(node.left)

            if prev:
                ans = min(ans, node.val - prev.val)
            prev = node
            dfs(node.right)
        
        dfs(root)
        return ans
        