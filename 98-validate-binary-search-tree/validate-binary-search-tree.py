# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# whebe ver we move left MIN , node.val right, node.val, MAX
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root,float("-inf"),float("inf"))
        
        
        
    def validate(self,node, left,right):
        if not node:
            return True
        
        if not node.val < right or not node.val >left:
            return False
        
        left = self.validate(node.left,left,node.val)
        right = self.validate(node.right,node.val , right)
        
        
        
        return left and right
#         inOrder = self._isValidBST(root)
#         print(inOrder)
        
#         if not inOrder:
#             return True
        
#         for i in range(1,len(inOrder)):
#             prev = inOrder[i-1]
#             curr = inOrder[i]
            
#             if curr > prev:
#                 continue
#             else:
#                 return False
#         return True
    
    
#     def _isValidBST(self,root):
#         if not root:
#             return []
        
#         left = self._isValidBST(root.left)
#         right = self._isValidBST(root.right)
#         return left + [root.val] + right
        