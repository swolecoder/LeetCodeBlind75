# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        #3 represnts and 
        # 2 represnts OR
        # 1 means True
        #0 means False

        def helper(node):
            if not node.left and not node.right:
                return node.val == 1
            
            left = helper(node.left)
            right = helper(node.right)

            #post order
            if node.val == 3:
                return left and right
            
            if node.val == 2:
                return left or right
        return helper(root)
            


