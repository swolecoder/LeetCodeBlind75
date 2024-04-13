# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None

        temp = []

        def dfs(node):
            nonlocal temp
            if not node:
                return 
            dfs(node.left)
            temp.append(node)
            dfs(node.right)
        
        dfs(root)

        data = sorted( n.val for n in temp)
        print(data)
        for i in range(len(data)):
            temp[i].val = data[i]

        