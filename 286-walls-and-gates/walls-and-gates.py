from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:

        empty = 2147483647
        dirs = [
            (-1,0),
            (1,0),
            (0,-1),
            (0,1)
        ]

        R = len(rooms)
        C=  len(rooms[0])
        q = deque([])
        visited = set()

        for r in range(R):
            for c in range(C):
                if rooms[r][c] == 0:
                    q.append((r,c,0))
                    visited.add((r,c))
        print(q)
        while q:
            r,c, step = q.popleft()
            print(r,c,step)

            
            if rooms[r][c] == empty:
                rooms[r][c] = step

            for r1, c1 in dirs:
                new_row = r1 + r
                new_col = c1 + c

                if 0 <= new_row < R and 0 <= new_col < C and (new_row, new_col) not in visited and rooms[new_row][new_col] == empty:
                    q.append((new_row, new_col, step+1))
                    visited.add((new_row, new_col))


















        
        