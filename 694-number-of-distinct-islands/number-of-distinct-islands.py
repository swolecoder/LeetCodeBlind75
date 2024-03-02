class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:

        R = len(grid)
        C = len(grid[0])
        unique = set()
        seen = set()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r,c) not in seen:
                    ans = self.dfs(grid,r,c,seen,[],r,c)
                    unique.add(tuple(ans))
               
        return len(unique)

    

    
    def dfs(self,grid, r,c, seen, ans, baseR, baseC):
        inbound_x = 0 <= r < len(grid)
        inbound_y = 0 <= c < len(grid[0])

        if not inbound_x or not inbound_y or grid[r][c] == 0 or (r,c) in seen:
            return ans
        
        ans.append((r-baseR,c-baseC))
        seen.add((r,c))

        self.dfs(grid,r+1,c,seen,ans,baseR, baseC)
        self.dfs(grid,r,c-1,seen,ans,baseR, baseC)
        self.dfs(grid,r,c+1,seen,ans,baseR, baseC)
        self.dfs(grid,r-1,c,seen,ans,baseR, baseC)

        return ans

        

        