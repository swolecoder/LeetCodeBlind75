from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        degrees = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)  # The edge is from b to a
            degrees[a] += 1  # Increment the in-degree of a

        # Initialize the queue with all courses having no prerequisites (degree 0)
        q = deque([i for i in range(numCourses) if degrees[i] == 0])
        ans = []

        while q:
            node = q.popleft()
            ans.append(node)

            for nei in graph[node]:
                degrees[nei] -= 1  # Decrease the in-degree
                if degrees[nei] == 0:  # If no more prerequisites, add to queue
                    q.append(nei)

        # If all courses are processed, return the order, otherwise return an empty list
        return ans if len(ans) == numCourses else []
