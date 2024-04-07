# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict, deque
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        map = defaultdict(list)
        minValue = float("inf")
        maxValue = float("-inf")
        if not root:
            return []


        def bfs(node, level):
            q = deque([(node, level)])
            nonlocal minValue 
            nonlocal maxValue 

            # if not node:
            #     return
            
            # minValue = min(minValue, level)
            # maxValue = max(maxValue, level)
            # map[level].append(node.val)
            # dfs(node.left, level-1)
            # dfs(node.right, level +1)

            while q:
                n, l = q.popleft()
                minValue = min(minValue, l)
                maxValue = max(maxValue, l)
                map[l].append(n.val)

                if n.left:
                    q.append((n.left, l -1))
                if n.right:
                    q.append((n.right, l +1))


        
        bfs(root, 0)
        ans = []

        for i in range(minValue, maxValue+1):
            if i in map:
                ans.append(map[i])
        return ans

