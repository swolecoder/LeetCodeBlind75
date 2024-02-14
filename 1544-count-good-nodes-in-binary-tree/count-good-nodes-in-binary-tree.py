# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        q = deque([(root, float("-inf"))])

        ans = 0
        while q:
            node, prevMax = q.popleft()

            if node.val >= prevMax:
                ans +=1
            
            if node.left:
                q.append((node.left, max(node.val, prevMax)))
            if node.right:
                q.append((node.right, max(node.val, prevMax)))
        
        return ans 