# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        ans = 0
        q = deque([(root, root.val)])

        while q:

            node,maxVal = q.popleft()

            if node.val >= maxVal:
                ans +=1
            
            if node.left:
                q.append((node.left, max(node.val,maxVal)))
            if node.right:
                q.append((node.right, max(node.val,maxVal)))




        
        return ans
        