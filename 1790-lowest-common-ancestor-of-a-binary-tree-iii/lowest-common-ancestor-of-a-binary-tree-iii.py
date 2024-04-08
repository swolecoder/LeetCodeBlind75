"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # seen = set()

        # while p:
        #     seen.add(p)
        #     p = p.parent 
        
        # while q:
        #     if q in seen:
        #         return q
        #     q = q.parent 

        p1 = p
        q1 = q

        while p1 != q1:
            p1 = p1.parent if p1 else q
            q1 = q1.parent if q1 else p
        return p1