# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return ans

        def dfs(node, level):
            nonlocal ans

            if not node:
                return None
            
            if len(ans) == level:
                ans.append(node.val)
            
            dfs(node.right, level+1)
            dfs(node.left, level +1)
        
        dfs(root, 0)
        return ans
        