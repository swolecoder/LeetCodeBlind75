# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        map = defaultdict(list)

        def helper(node,level, map):
            if not node:
                return None
            
            map[level].append(node.val)

            helper(node.left, level +1, map)
            helper(node.right, level +1, map)
        
        helper(root, 0, map)

        return map.values()
        