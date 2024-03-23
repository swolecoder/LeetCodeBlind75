from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        seen = [False] * len(rooms)

        q = deque([0])
        seen[0] = True

        
        while q:
            node = q.popleft()
            print(node)
            print(rooms[node])

            for nei in rooms[node]:
                if seen[nei] != True:
                    q.append(nei)
                    seen[nei] = True
        

        print(seen)
        if all(seen):
            return True
        
        return False



       

        