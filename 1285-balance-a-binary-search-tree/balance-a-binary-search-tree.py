# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        data = []

        def inOrder(root):
            nonlocal data

            if not root:
                return 
            
            inOrder(root.left)
            data.append(root.val)
            inOrder(root.right)
        
        inOrder(root)

        print(data)

        def buildTree(arr):

            if not arr:
                return None
            middle = len(arr) //2

            root = TreeNode(arr[middle])
            root.left = buildTree(arr[0:middle])
            root.right = buildTree(arr[middle+1:])
            return root
        
        return buildTree(data)
        