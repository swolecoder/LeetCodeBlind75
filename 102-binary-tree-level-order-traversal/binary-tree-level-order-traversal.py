# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        map = defaultdict(list)

        q = [(root ,0)]


        while q:

            data = q.pop(0)
            val, level = data[0], data[1]
            map[level].append(val.val)

            if val.left:
                q.append((val.left, level +1))
            if val.right:
                q.append((val.right, level +1))
        print(map)
        return [ v for k, v in map.items()]
        
        # return  [v] for k,v in map.items()
