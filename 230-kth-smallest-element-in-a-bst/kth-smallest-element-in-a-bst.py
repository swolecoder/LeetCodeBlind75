# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        count = 0
        val = None
        def helper(root):
            nonlocal count
            nonlocal val

            if not root:
                return None
            
            helper(root.left)

            count +=1

            if count == k:
                val = root.val
                return 
            
            helper(root.right)


        helper(root)

        return val

            
        