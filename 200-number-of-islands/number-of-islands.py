class UF:
    def __init__(self,grid):
        r , c = len(grid), len(grid[0])
        self.state = [-1] * (r*c)
        self.count = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1":
                    self.state[i*c +j] = i *c + j
                    self.count +=1
    
    def find(self, a):
        if self.state[a] != a:
            self.state[a] = self.find(self.state[a])
        return self.state[a]
    
    def union(self,a,b):
        A = self.find(a)
        B = self.find(b)

        if A != B:
            self.state[B] = A
            self.count -=1



class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        uf = UF(grid)
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        r = len(grid)
        c = len(grid[0])

        for i in range(r):
            for j in range(c):
                if grid[i][j] =="1":
                    for x,y in dirs:
                        new_x, new_y = i + x, j + y
                        if 0<= new_x < r and 0 <= new_y < c and grid[new_x][new_y] == "1":
                            uf.union(i*c+j, new_x *c + new_y)
        return uf.count 
        