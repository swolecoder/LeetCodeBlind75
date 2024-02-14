# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        return self._maxDepth(root)
    


    def _maxDepth(self, node):
        if not node:
            return 0
        
        left = self._maxDepth(node.left)
        right = self._maxDepth(node.right)

        return max(left, right) + 1
        