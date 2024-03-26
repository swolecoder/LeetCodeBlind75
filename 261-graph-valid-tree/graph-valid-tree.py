from collections import defaultdict
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
        
        # uf = UF(edges, n)

        # for a,b in edges:
        #     if uf.union(a,b) == False:
        #         return False
        
        # return True

        map = defaultdict(list)
        for a, b in edges:
            map[a].append(b)
            map[b].append(a)
        seen = set()
        
        def dfs(node, previos):
            if node in seen:
                return False

            seen.add(node)

            for nei in map[node]:
                if nei != previos and dfs(nei,node) == False:
                    return False
            
            return True
        
              # Start DFS from node 0 (arbitrarily chosen)
        if not dfs(0, -1):
            return False
        
        return  len(seen) == n
    




        