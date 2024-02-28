from collections import defaultdict, deque
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
    #  stopID -> busses that stop three
    #  1 -> 0 
    #  2 -> 0 
    #  7 -> 0 , 1
    #  3 -> 1 
    #  6 -> 1

        graph = defaultdict(list)
        seen = set()
        for i in range(len(routes)):
            busId = i 
            for j in range(len(routes[i])):
                graph[routes[i][j]].append(busId)
        print(graph)

        q = deque([(source, 0)])



        seen_stop = set()
        seen_bus = set()
        while q:
            current, bus_taken = q.popleft()

            if current == target:
                return bus_taken
            key = (current,bus_taken)

            for nei in graph[current]:
                if nei not in seen_bus:
                    seen_bus.add(nei)

                    for stop in routes[nei]:
                        if stop not in seen_stop:
                            q.append((stop,bus_taken+1))
                            seen_stop.add(stop)



        return -1



        