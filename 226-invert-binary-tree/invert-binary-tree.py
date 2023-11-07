# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return None
        
        head = root

        q = [root]

        while q:

            data = q.pop(0)
            temp = data.left if data.left else None
            data.left = data.right if data.right else None
            data.right = temp

            if data.left:
                q.append(data.left)
            if data.right:
                q.append(data.right)
        return head
        