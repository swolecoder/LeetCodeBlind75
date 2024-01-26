class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        map = defaultdict(list)

        for i in range(n):
            map[i].append(rooms[i])
        print(map)      

        seen = set()
        def dfs(room):

            if room in seen:
                return 

            seen.add(room)

            for r in map[room]:
                for i in r:
                    if i not in seen:
                        dfs(i) 

        dfs(0)
        print(seen)
        return len(seen) == n 