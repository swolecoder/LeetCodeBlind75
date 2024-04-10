from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1
        dirs = [
        [0, 1],
        [0, -1],
        [1, 0],
        [-1, 0],
        [1, 1],
        [-1, -1],
        [1, -1],
        [-1, 1]
        ]


        print("Hello")

        R = len(grid) -1
        C = len(grid[0])-1

        q = deque([(0,0, 1)])

        seen = set()

        while q:
            r,c,level = q.popleft()

            if r == R and c == C and grid[-1][-1] == 0:
                return level
            

            for r1,c1 in dirs:

                row = r1 + r
                col = c1 +c

                if 0<= row < len(grid) and 0 <= col < len(grid[0]) and (row,col) not in seen and grid[row][col] == 0:
                    q.append((row,col, level+1))
                    seen.add((row,col))
        

        return -1
            

            




        