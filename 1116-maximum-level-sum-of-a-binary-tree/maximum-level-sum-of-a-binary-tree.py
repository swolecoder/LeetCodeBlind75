# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        

        ansSum , ansLevel = float('-inf'), 0

        q = []
        q.append(root)
        level = 0

        while q:
            l = len(q)
            sum = 0
            level +=1

            for i in range(l):
                node = q.pop(0)
                sum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if sum > ansSum:
                ansLevel = level
                ansSum = sum 
        return ansLevel

