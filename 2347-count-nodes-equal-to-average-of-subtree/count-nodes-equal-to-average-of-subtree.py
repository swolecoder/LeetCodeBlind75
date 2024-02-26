# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.found = 0
    def averageOfSubtree(self, root: TreeNode) -> int:
        
        self._averageOfSubtree(root)
        return self.found 
    

    def _averageOfSubtree(self,root):

        if not root:
            return [0,0] # sum , seen 
        left = self._averageOfSubtree(root.left)
        right = self._averageOfSubtree(root.right)

        total = root.val + left[0] + right[0]
        node_seen = left[1] + right[1] + 1
        cal = total // node_seen
        if cal == root.val:
            self.found +=1
        return [ total , node_seen]

