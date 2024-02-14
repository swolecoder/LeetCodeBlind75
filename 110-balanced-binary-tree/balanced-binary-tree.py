# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self._isBalanced(root)[0]


    def _isBalanced(self, root):

        if not root:
            return [True, 0]
        left = self._isBalanced(root.left)
        right = self._isBalanced(root.right)
        cal = left[0] and right[0] and abs(left[1] - right[1]) < 2
        return [cal , max(left[1], right[1]) +1]
    