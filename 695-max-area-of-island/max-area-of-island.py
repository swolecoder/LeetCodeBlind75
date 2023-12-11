class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def dfs(r,c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 0:
                return 0
            

            grid[r][c] = 0
            count = 1

            count += dfs(r-1,c)
            count +=dfs(r +1, c)
            count +=  dfs(r, c-1)
            count += dfs(r,c+1)
            return count


        ans = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]:
                    ans = max(ans, dfs(r,c))
            
        return ans

        