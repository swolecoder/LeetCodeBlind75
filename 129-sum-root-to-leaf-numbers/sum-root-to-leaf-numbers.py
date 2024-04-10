# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = []

        if not root:
            return []

        q = deque([(root, root.val)])

        while q:
            node , total = q.popleft()
            print(node,total)

            if not node.left and not node.right:
                ans.append(total)
            if node.left:
                q.append((node.left, total * 10 + node.left.val))
            if node.right:
                q.append((node.right, total * 10 + node.right.val))
        
        print(ans)
        return sum(ans)
        


