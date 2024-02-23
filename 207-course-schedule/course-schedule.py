from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashMap = {i : [] for i in range(numCourses)}

        for a,b in prerequisites:
            hashMap[b].append(a)

        visited = set()
        print(hashMap)

        def dfs(node):
            if node in visited:
                return False
            if hashMap[node] == []:
                return True
            
            visited.add(node)
            for nei in hashMap[node]:
                if dfs(nei) == False:
                    return False
            visited.remove(node)
            hashMap[node] = []
            return True
        
        for k in range(numCourses):
            # print(k)
            if dfs(k) == False:
                return False
        return True

        