class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    self.sinkIsland(grid, i, j, m, n)
        
        return count


    
    def sinkIsland(self, grid, row, col, m, n):
        if row < 0 or row >= m or col < 0 or col >= n or grid[row][col] == '0':
            return

        grid[row][col] = '0'
        self.sinkIsland(grid, row - 1, col, m, n)
        self.sinkIsland(grid, row + 1, col, m, n)
        self.sinkIsland(grid, row, col- 1, m, n)
        self.sinkIsland(grid, row, col + 1, m, n)
