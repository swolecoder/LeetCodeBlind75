# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        ans = 0

        q = [(root, 1)]

        while q:
            data = q.pop(0)
            h = data[1]

            ans = max(ans, h)

            if data[0].left:
                q.append((data[0].left, h +1))
            if data[0].right:
                q.append((data[0].right, h +1))
        
        return ans


        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        