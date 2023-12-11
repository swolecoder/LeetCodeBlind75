class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        r = len(grid)
        c = len(grid[0])
        ans = 0


        def dfs(i, j):
            if i < 0 or j < 0 or i >= r or j >= c or grid[i][j] != "1":
                return 
            
            grid[i][j] = "*" #mark this as visited

            dfs(i+1, j)
            dfs(i, j+1)
            dfs(i-1, j)
            dfs(i, j -1)

        
        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1":
                    ans +=1
                    dfs(i,j)
        return ans
        