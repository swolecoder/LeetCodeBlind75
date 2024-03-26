class UF:
    def __init__(self,edges,n):
        self.parent = [i for i in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]
    
    def union(self, x,y):
        A = self.find(x)
        B = self.find(y)

        if A == B:
            return False
        
        self.parent[B] = A


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        uf = UF(edges, n)

        for a,b in edges:
            if uf.union(a,b) == False:
                return False
        
        return True
    

        