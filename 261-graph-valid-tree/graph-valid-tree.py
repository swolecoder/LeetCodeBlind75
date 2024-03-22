class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = [ i for i in range(n)]

        if len(edges) != n-1:
            return False

        def find(a):
            if parent[a] != a:
                parent[a] = find(parent[a])
            
            return parent[a]
        
        def union(a,b):
            A = find(a)
            B = find(b)

            if A == B:
                return False
            
            parent[B] = A

            return True
        

        for a, b in edges:
            if not union(a,b):
                return False
        
        return True
        