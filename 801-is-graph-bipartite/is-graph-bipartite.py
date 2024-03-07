from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        g = self.buildGraph(graph)
        seen = {}

        for k in g.keys():

            if k not in seen and self.dfs(g,k,-1,False, seen) == False:
                return False
        return True
        
    def buildGraph(self, graph):
        map = defaultdict(list)
        for i in range(len(graph)):
            
            for j in range(len(graph[i])):
                map[i].append(graph[i][j])
        return map
        
    def dfs(self, graph, node, lastNode, color, seen):
        if node in seen:
            return seen[node] == color
        
        seen[node] = color
        
        for nei in graph[node]:
            if self.dfs(graph, nei,node,not color, seen) == False:
                return False
        
        return True