# The given code for solving the "Number of Islands" problem employs a Depth-First Search (DFS) approach to identify and count islands in a 2D grid. This method works by iterating over each cell in the grid and, upon finding a land cell ("1"), using a recursive helper function to visit all adjacent land cells, marking them as visited ("*") to avoid recounting. This effectively "sinks" an island by converting all its land cells to a different marker as it encounters them, ensuring that each island is counted exactly once.

# ### Time Complexity of DFS Approach

# - **Best and Average Case:** The time complexity of the DFS approach is \(O(R \times C)\), where \(R\) and \(C\) are the numbers of rows and columns in the grid, respectively. This is because, in the worst case, the algorithm needs to visit every cell in the grid once.

# ### Union-Find Approach and Its Advantages

# The Union-Find algorithm, on the other hand, offers a different mechanism for solving the same problem, potentially with some performance benefits under certain conditions.

# - **Initialization:** \(O(R \times C)\) for setting up the Union-Find data structure, with each cell initially considered its own set.
# - **Union Operations:** Potentially less than \(O(R \times C)\) if the grid is sparse or if islands are large, as the algorithm quickly merges adjacent cells of an island into a single set, reducing the number of operations needed in future merges.
# - **Find Operations:** Amortized near \(O(1)\) due to path compression, making the process of checking and merging sets very efficient.

# ### Advantages of Union-Find Over DFS

# 1. **Path Compression:** Union-Find with path compression makes the find operation almost constant time, which is particularly efficient when the grid is large and sparsely populated with islands.

# 2. **Non-Recursive:** Unlike DFS, which can hit recursion depth limits on large grids or for large islands, Union-Find is iterative and doesn't suffer from stack overflow issues.

# 3. **Analyzing Connectivity:** Union-Find explicitly tracks connectivity and disjoint sets, which can be more intuitive for understanding the structure of the grid's islands, especially if modifications or queries on the structure are needed after the initial pass.

# ### When Is DFS Preferable?

# DFS is simpler to implement and understand for the "Number of Islands" problem. It's very direct and can be faster for grids with lots of small islands due to its straightforward recursive exploration. It doesn't require the overhead of maintaining a separate data structure or the initial pass to set up the Union-Find structure.

# ### Conclusion

# - **DFS Approach:** Best for simplicity and directness, especially with many small islands or dense grids. It's also stack-bound due to recursion, which can be a limiting factor on very large grids.
# - **Union-Find Approach:** Offers a non-recursive, potentially more efficient solution for sparse grids or when dealing with operations beyond just counting islands (like dynamically modifying the grid and querying island connectivity). It can handle larger datasets without hitting stack limits and provides a clear framework for understanding the connectivity of elements in the grid.

# The choice between DFS and Union-Find depends on the specific requirements of your application, including the size of the input grid, the density of islands, and the need for additional operations on the grid.

class UF:
    def __init__(self,grid):
        r,c = len(grid), len(grid[0])
        self.count = 0
        self.state= [-1] * (r*c)

        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1":
                    self.count +=1
                    self.state[i*c+j] = i*c+j
    def find(self,i):
        if self.state[i] != i:
            self.state[i] = self.find(self.state[i])
        return  self.state[i] 
    def Union(self,a,b):
        x = self.find(a)
        y = self.find(b)
        if x != y:
            self.state[y] = x
            self.count -=1

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        uf = UF(grid)

        
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        r = len(grid)
        c = len(grid[0])

        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1":
                    for x,y in dirs:
                        inbound_x, inbound_y = 0<= x+i < r , 0<=y+j< c
                        new_x, new_y = x+i, y+j
                        if inbound_x and inbound_y and grid[new_x][new_y] == "1":
                            uf.Union(i*c+j , new_x * c + new_y)
        print(uf.count)
        print(uf.state)
        return uf.count


        # R = len(grid)
        # C = len(grid[0])

        # def helper(r,c):
        #     if r >= R or c >= C or r < 0 or c < 0 or grid[r][c] != "1":
        #         return 

        #     grid[r][c] = "*"

        #     helper(r+1,c)
        #     helper(r -1,c)
        #     helper(r,c-1)
        #     helper(r,c+1)

        # res = 0

        # for i in range(R):
        #     for j in range(C):
        #         if grid[i][j] == "1":
        #             helper(i,j)
        #             res +=1
        # return res        