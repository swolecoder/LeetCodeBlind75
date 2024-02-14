# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def helper(root, leftMax= float("-inf"), rightMax =float("inf")):
            if not root:
                return True
            
            # check
            if not(root.val > leftMax and root.val < rightMax):
                return False

            left = helper(root.left, leftMax, root.val)
            right = helper(root.right, root.val, rightMax)

            return left and right
        return helper(root)

#     - 100 , 100

#             2
#       1.                 3
# -100, Node.val       Node.val , 100(Keep as parent)  
