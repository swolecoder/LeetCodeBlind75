# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def helper(root, ans):
            if not root:
                return 
            if root and not root.left and not root.right:
                ans.append(root.val)
                return 
            
            helper(root.left,ans)
            helper(root.right,ans)
        ans1 = []
        ans2 = []

        helper(root1,ans1)
        helper(root2, ans2)
        print(ans1, ans2)
        return ans1 == ans2



        