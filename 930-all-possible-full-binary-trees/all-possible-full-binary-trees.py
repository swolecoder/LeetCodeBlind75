# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
            map = {}
            return self.dfs(n, map)

    def dfs(self,n, map):
        if n == 0:
            return []
        if n == 1:
            return [TreeNode(0)]
        
        if n == 2:
            return []
        
        ans = []
        if n in map:
            return map[n]

        for l in range(0,n):
            r = n - l - 1
            left = self.dfs(l,map)
            right = self.dfs(r,map)

            for t1 in left:
                for t2 in right:
                    ans.append(TreeNode(0,t1,t2))
        map[n] = ans
        return ans

        