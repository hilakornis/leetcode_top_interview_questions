class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def visited(grid, i, j, m, n):
            grid[i][j] = "2"
            if i+1 < m and grid[i+1][j] == "1":
                visited(grid, i+1, j, m, n)
            if i > 0 and grid[i-1][j] == "1":
                visited(grid, i-1, j, m, n)
            
            if j+1 < n and grid[i][j+1] == "1":
                visited(grid, i, j+1, m, n)
            if j > 0 and grid[i][j-1] == "1":
                visited(grid, i, j-1, m, n)
        
        m = len(grid)
        n = len(grid[0])
        counter = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    counter += 1
                    visited(grid, i, j, m, n)
                else:
                    grid[i][j] = "2"
                    
        return counter