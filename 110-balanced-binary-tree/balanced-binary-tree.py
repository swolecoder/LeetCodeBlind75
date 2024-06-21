# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def helper(node):
            if not node:
                return [True, 0]
            
            left = helper(node.left)
            right = helper(node.right)
            
            # if not left[0] or not right[0]:
            #     return [False, None]
            
            is_unbalanced = left[0] and right[0] and abs(left[1] - right[1]) < 2
            if not is_unbalanced :
                return [False, None]
            else:
            
                return [is_unbalanced, max(left[1], right[1]) + 1]
        
        return helper(root)[0]




        