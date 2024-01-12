class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        seen = set()

        def dfs(r,c):
            if r >= len(grid) or c >= len(grid[0]) or r < 0 or c < 0 or grid[r][c] == 0:
                return 1

            if (r,c) in seen:
                return 0

            seen.add((r,c))

            perm = dfs(r+1,c) 
            perm += dfs(r -1,c)
            perm += dfs(r,c+1)
            perm += dfs(r,c-1)
            return perm

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    return dfs(i,j)      