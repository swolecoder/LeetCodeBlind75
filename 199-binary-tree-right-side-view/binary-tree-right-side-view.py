# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        

        q = []

        q.append(root)
        ans = []

        while q:
            l = len(q)

            for i in range(l):
                n = q.pop(0)

                if i == l-1:
                    ans.append(n.val)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)

        
        return ans



        