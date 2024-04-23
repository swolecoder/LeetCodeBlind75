from collections import deque
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        dist_matrix = [[0] * C for _ in range(R)]
        dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        min_dist = float("inf")
        empty_land = 0

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    local_min = float("inf")
                    q = deque([(r, c, 0)])

                    while q:
                        r1, c1, distance = q.popleft()

                        for row, col in dirs:
                            new_row = r1 + row
                            new_col = c1 + col

                            if 0 <= new_row < R and 0 <= new_col < C and grid[new_row][new_col] == empty_land:
                                grid[new_row][new_col] -= 1
                                dist_matrix[new_row][new_col] += distance + 1
                                q.append((new_row, new_col, distance + 1))
                                local_min = min(local_min, dist_matrix[new_row][new_col])

                    min_dist = local_min
                    empty_land -= 1

        return -1 if min_dist == float("inf") else min_dist

        