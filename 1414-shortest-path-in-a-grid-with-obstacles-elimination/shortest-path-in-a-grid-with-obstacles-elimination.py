from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        R = len(grid)
        C = len(grid[0])

        seen = set()

        q = deque([(0,0,k,0)]) # r, c, k -> obstacles and steps
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        seen.add((0,0,k))

        while q:
            r,c,left, step = q.popleft()

            if r == R-1 and c == C-1:
                return step
            if grid[r][c] == 1: 
                left -=1
             
            for r1,c1 in dirs:
                new_row, new_col = r1 + r , c1 + c

                if 0 <= new_row < R and 0 <= new_col < C and (new_row,new_col,left) not in seen and left >= 0:
                    q.append((new_row,new_col,left, step +1))
                    seen.add((new_row,new_col,left))
        return -1


        