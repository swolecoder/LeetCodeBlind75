from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        
        def build_graph(edges):
            map = defaultdict(list)

            for a,b in edges:
                map[a].append(b)
                map[b].append(a)
            return map
        
        graph = build_graph(edges)
        print(graph)


        def dfs(graph, node, seen):
            if node in seen:
                return None
            seen.add(node)
            if node == destination:
                return True
            
            for nei in graph[node]:
                if nei not in seen:
                    if dfs(graph,nei, seen) == True:
                        return True
            
            return False

        return dfs(graph, source, set())




        # print("Ashish")

        