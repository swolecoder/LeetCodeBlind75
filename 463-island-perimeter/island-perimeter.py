class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        seen = set()
        R = len(grid)
        C = len(grid[0])


        def dfs(r,c):
            if r < 0 or c < 0 or r >= R or c >= C or grid[r][c] == 0:
                return 1
            
            if (r,c) in seen :
                return 0 
            seen.add((r,c))

            ans =  dfs(r -1,c)
            ans += dfs(r+1,c)
            ans += dfs(r, c-1)
            ans += dfs(r,c+1)
            return ans
        

        for i in range(R):
            for j in range(C):
                if grid[i][j]:
                    return dfs(i,j)
        
        