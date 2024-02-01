# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        map = defaultdict(list)

        if not root:
            return []

        q = [(root, 0)]

        while q:
            node, level = q.pop(0)
            map[level].append(node.val)
            if node.left:
                q.append((node.left, level -1))
            if node.right:
                q.append((node.right, level+1))
        return [ map[data] for data in sorted(map.keys())]
        