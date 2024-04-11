# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        map = defaultdict(list)

        if not root:
            return None

        def dfs(x,y,node):
            if not node:
                return 
                        
            dfs(x-1, y+1, node.left)
            dfs(x+1, y+1, node.right)
            map[(x,y)].append(node.val)
        
        dfs(0,0,root)
        print(map)

    
        ans = []
        old = float('-inf')
        
        # vertical_positions = sorted(set(k[0] for k in map.keys()))  # Get distinct vertical positions and sort them
        # ans = [[] for _ in range(len(vertical_positions))] 
        for k,v in sorted(map.items()):
            
            if k[0] != old:
                ans.append([])
            ans[-1].extend(sorted(v))
            old = k[0]
        return ans