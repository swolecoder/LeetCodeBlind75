# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        min_seen = float('inf')
        val = None

        def helper(node, target):
            nonlocal min_seen, val
            if not node:
                return
            diff = abs(node.val - target)
            if diff < min_seen:
                min_seen = diff
                val = node.val
            elif diff == min_seen and node.val < val:
                val = node.val

            if node.val < target:
                helper(node.right, target)
            else:
                helper(node.left, target)

        helper(root, target)
        return val
            



        