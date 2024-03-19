# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not preorder:
            return None
        
        root = TreeNode(preorder[0])

        mid = inorder.index(preorder[0])
        left_val = inorder[:mid]
        right_val = inorder[mid+1:]
        size = len(left_val)
        root.left = self.buildTree(preorder[1: size+1], left_val)
        root.right = self.buildTree(preorder[size+1:], right_val)
        return root
